#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = Path(__file__).resolve().parent / "validator.yaml"


errors: list[str] = []
warnings: list[str] = []


def load_yaml(path: Path) -> Any:
    """Load a YAML file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as exc:
        add_error(path, f"Invalid YAML: {exc}")
        return None
    except OSError as exc:
        add_error(path, f"Unable to read file: {exc}")
        return None


def relative_path(path: Path) -> str:
    """Return a repository-relative path."""
    try:
        return str(path.relative_to(REPOSITORY_ROOT))
    except ValueError:
        return str(path)


def add_error(path: Path | str, message: str) -> None:
    """Register a validation error."""
    errors.append(f"ERROR: {relative_path(Path(path))}: {message}")


def add_warning(path: Path | str, message: str) -> None:
    """Register a validation warning."""
    warnings.append(f"WARNING: {relative_path(Path(path))}: {message}")


def require_mapping(
    path: Path,
    data: Any,
    field_name: str,
) -> dict[str, Any] | None:
    """Validate that a value is a YAML mapping."""
    if not isinstance(data, dict):
        add_error(path, f"'{field_name}' must be a mapping.")
        return None

    return data


def require_list(
    path: Path,
    data: Any,
    field_name: str,
) -> list[Any] | None:
    """Validate that a value is a YAML list."""
    if not isinstance(data, list):
        add_error(path, f"'{field_name}' must be a list.")
        return None

    return data


def load_controlled_ids(
    path: Path,
    root_key: str,
) -> set[str]:
    """Load IDs from a controlled vocabulary file."""
    data = load_yaml(path)

    if not isinstance(data, dict):
        return set()

    items = data.get(root_key)

    if not isinstance(items, list):
        add_error(path, f"'{root_key}' must be a list.")
        return set()

    result: set[str] = set()

    for item in items:
        if not isinstance(item, dict):
            add_error(path, f"Each item in '{root_key}' must be a mapping.")
            continue

        item_id = item.get("id")

        if not isinstance(item_id, str) or not item_id:
            add_error(path, f"Each item in '{root_key}' must have a valid id.")
            continue

        if item_id in result:
            add_error(path, f"Duplicate controlled ID '{item_id}'.")

        result.add(item_id)

    return result


def load_status_ids(
    path: Path,
) -> set[str]:
    """Load status names from a status schema."""
    data = load_yaml(path)

    if not isinstance(data, dict):
        return set()

    statuses = data.get("statuses")

    if not isinstance(statuses, dict):
        add_error(path, "'statuses' must be a mapping.")
        return set()

    return set(statuses.keys())


def validate_multilingual_field(
    path: Path,
    field_name: str,
    value: Any,
    required_languages: list[str],
) -> None:
    """Validate a multilingual mapping."""
    if not isinstance(value, dict):
        add_error(path, f"'{field_name}' must be a multilingual mapping.")
        return

    for language in required_languages:
        if language not in value:
            add_error(
                path,
                f"'{field_name}' is missing language '{language}'.",
            )


def validate_date(
    path: Path,
    field_name: str,
    value: Any,
) -> None:
    """Validate an ISO 8601 date."""
    if value in (None, ""):
        add_warning(path, f"'{field_name}' is empty.")
        return

    if not isinstance(value, str):
        add_error(path, f"'{field_name}' must be a string in YYYY-MM-DD format.")
        return

    try:
        date.fromisoformat(value)
    except ValueError:
        add_error(path, f"'{field_name}' is not a valid ISO date: '{value}'.")


def validate_bottlenecks(
    path: Path,
    data: Any,
    config: dict[str, Any],
    id_pattern: re.Pattern[str],
    required_languages: list[str],
) -> None:
    """Validate bottleneck structures when present."""
    if data is None:
        return

    if not isinstance(data, list):
        add_error(path, "'bottlenecks' must be a list.")
        return

    required_fields = config["required_fields"]
    impact_levels = set(config["impact_levels"])

    for index, item in enumerate(data):
        location = f"bottlenecks[{index}]"

        if not isinstance(item, dict):
            add_error(path, f"'{location}' must be a mapping.")
            continue

        for field in required_fields:
            if field not in item:
                add_error(path, f"'{location}' is missing required field '{field}'.")

        item_id = item.get("id")

        if isinstance(item_id, str) and not id_pattern.fullmatch(item_id):
            add_error(path, f"'{location}.id' is invalid: '{item_id}'.")

        if "description" in item:
            validate_multilingual_field(
                path,
                f"{location}.description",
                item["description"],
                required_languages,
            )

        impact = item.get("impact")

        if impact is not None:
            if not isinstance(impact, dict):
                add_error(path, f"'{location}.impact' must be a mapping.")
            else:
                level = impact.get("level")

                if level not in impact_levels:
                    add_error(
                        path,
                        f"'{location}.impact.level' must be one of: "
                        f"{', '.join(sorted(impact_levels))}.",
                    )


def validate_failure_modes(
    path: Path,
    data: Any,
    config: dict[str, Any],
    id_pattern: re.Pattern[str],
    required_languages: list[str],
) -> None:
    """Validate failure mode structures when present."""
    if data is None:
        return

    if not isinstance(data, list):
        add_error(path, "'failure_modes' must be a list.")
        return

    required_fields = config["required_fields"]
    severity_levels = set(config["severity_levels"])

    for index, item in enumerate(data):
        location = f"failure_modes[{index}]"

        if not isinstance(item, dict):
            add_error(path, f"'{location}' must be a mapping.")
            continue

        for field in required_fields:
            if field not in item:
                add_error(path, f"'{location}' is missing required field '{field}'.")

        item_id = item.get("id")

        if isinstance(item_id, str) and not id_pattern.fullmatch(item_id):
            add_error(path, f"'{location}.id' is invalid: '{item_id}'.")

        if "description" in item:
            validate_multilingual_field(
                path,
                f"{location}.description",
                item["description"],
                required_languages,
            )

        for field in ("causes", "effects"):
            if field in item and not isinstance(item[field], list):
                add_error(path, f"'{location}.{field}' must be a list.")

        severity = item.get("severity")

        if severity not in severity_levels:
            add_error(
                path,
                f"'{location}.severity' must be one of: "
                f"{', '.join(sorted(severity_levels))}.",
            )


def validate_entity(
    path: Path,
    data: Any,
    expected_type: str,
    config: dict[str, Any],
    valid_phases: set[str],
    valid_categories: set[str],
    valid_evidence_statuses: set[str],
    valid_completeness_statuses: set[str],
    known_entity_ids: set[str],
) -> str | None:
    """Validate a single knowledge entity and return its ID."""
    if not isinstance(data, dict):
        add_error(path, "Entity must be a YAML mapping.")
        return None

    validation = config["validation"]

    required_languages = validation["multilingual"]["required_languages"]
    id_pattern = re.compile(validation["id"]["pattern"])

    for field in validation["required_common_fields"]:
        if field not in data:
            add_error(path, f"Missing required field '{field}'.")

    entity_id = data.get("id")

    if not isinstance(entity_id, str) or not entity_id:
        add_error(path, "'id' must be a non-empty string.")
    elif not id_pattern.fullmatch(entity_id):
        add_error(path, f"Invalid canonical ID '{entity_id}'.")

    if data.get("type") != expected_type:
        add_error(
            path,
            f"Expected type '{expected_type}', found '{data.get('type')}'.",
        )

    if isinstance(entity_id, str) and entity_id:
        if path.stem != entity_id:
            add_error(
                path,
                f"Filename '{path.stem}' must match canonical ID '{entity_id}'.",
            )

    for field in ("name", "summary"):
        if field in data:
            validate_multilingual_field(
                path,
                field,
                data[field],
                required_languages,
            )

    status = data.get("status")

    if isinstance(status, dict):
        for field in validation["required_status_fields"]:
            if field not in status:
                add_error(path, f"status is missing required field '{field}'.")

        evidence = status.get("evidence")
        completeness = status.get("completeness")

        if evidence not in valid_evidence_statuses:
            add_error(path, f"Invalid evidence status '{evidence}'.")

        if completeness not in valid_completeness_statuses:
            add_error(path, f"Invalid completeness status '{completeness}'.")

    elif status is not None:
        add_error(path, "'status' must be a mapping.")

    phase = data.get("phase")

    if isinstance(phase, dict):
        for field in validation["required_phase_fields"]:
            if field not in phase:
                add_error(path, f"phase is missing required field '{field}'.")

        for field in (
            "expected",
            "earliest_plausible",
            "latest_plausible",
        ):
            value = phase.get(field)

            if value is not None and value not in valid_phases:
                add_error(path, f"Invalid phase '{value}' in phase.{field}.")

    elif phase is not None:
        add_error(path, "'phase' must be a mapping.")

    categories = data.get("categories")

    if categories is not None:
        if not isinstance(categories, list):
            add_error(path, "'categories' must be a list.")
        else:
            for category in categories:
                if category not in valid_categories:
                    add_error(path, f"Unknown category '{category}'.")

    sources = data.get("sources")

    if sources is not None and not isinstance(sources, list):
        add_error(path, "'sources' must be a list.")

    metadata = data.get("metadata")

    if isinstance(metadata, dict):
        for field in validation["required_metadata_fields"]:
            if field not in metadata:
                add_error(path, f"metadata is missing required field '{field}'.")

        validate_date(path, "metadata.created", metadata.get("created"))
        validate_date(path, "metadata.updated", metadata.get("updated"))

    elif metadata is not None:
        add_error(path, "'metadata' must be a mapping.")

    validate_bottlenecks(
        path,
        data.get("bottlenecks"),
        validation["bottlenecks"],
        id_pattern,
        required_languages,
    )

    validate_failure_modes(
        path,
        data.get("failure_modes"),
        validation["failure_modes"],
        id_pattern,
        required_languages,
    )

    return entity_id if isinstance(entity_id, str) else None


def collect_entity_files(
    config: dict[str, Any],
) -> list[tuple[Path, str]]:
    """Collect all entity files and their expected types."""
    result: list[tuple[Path, str]] = []

    for entity_config in config["entities"].values():
        directory = REPOSITORY_ROOT / entity_config["path"]
        expected_type = entity_config["type"]

        if not directory.exists():
            add_error(directory, "Required entity directory does not exist.")
            continue

        for path in sorted(directory.glob("*.yaml")):
            result.append((path, expected_type))

    return result


def main() -> int:
    """Run repository validation."""
    if not CONFIG_PATH.exists():
        print(f"ERROR: Configuration file not found: {CONFIG_PATH}")
        return 1

    config = load_yaml(CONFIG_PATH)

    if not isinstance(config, dict):
        print("ERROR: Invalid validator configuration.")
        return 1

    schema_paths = config["schemas"]

    phases_path = REPOSITORY_ROOT / schema_paths["phases"]
    evidence_path = REPOSITORY_ROOT / schema_paths["evidence_statuses"]
    completeness_path = REPOSITORY_ROOT / schema_paths["completeness_statuses"]
    categories_path = REPOSITORY_ROOT / schema_paths["categories"]

    valid_phases = load_controlled_ids(phases_path, "phases")
    valid_categories = load_controlled_ids(categories_path, "categories")
    valid_evidence_statuses = load_status_ids(evidence_path)
    valid_completeness_statuses = load_status_ids(completeness_path)

    entity_files = collect_entity_files(config)

    entity_data: list[tuple[Path, Any, str]] = []
    known_entity_ids: set[str] = set()
    entity_id_locations: dict[str, Path] = {}

    for path, expected_type in entity_files:
        data = load_yaml(path)

        if not isinstance(data, dict):
            continue

        entity_id = data.get("id")

        if isinstance(entity_id, str) and entity_id:
            if entity_id in entity_id_locations:
                add_error(
                    path,
                    f"Duplicate entity ID '{entity_id}'. "
                    f"Already used in {relative_path(entity_id_locations[entity_id])}.",
                )
            else:
                entity_id_locations[entity_id] = path
                known_entity_ids.add(entity_id)

        entity_data.append((path, data, expected_type))

    for path, data, expected_type in entity_data:
        validate_entity(
            path=path,
            data=data,
            expected_type=expected_type,
            config=config,
            valid_phases=valid_phases,
            valid_categories=valid_categories,
            valid_evidence_statuses=valid_evidence_statuses,
            valid_completeness_statuses=valid_completeness_statuses,
            known_entity_ids=known_entity_ids,
        )

    print()

    if warnings:
        print("WARNINGS")
        print("-" * 60)

        for warning in warnings:
            print(warning)

        print()

    if errors:
        print("VALIDATION FAILED")
        print("-" * 60)

        for error in errors:
            print(error)

        print()
        print(f"Errors: {len(errors)}")
        print(f"Warnings: {len(warnings)}")

        return 1

    print("VALIDATION PASSED")
    print("-" * 60)
    print(f"Validated entity files: {len(entity_data)}")
    print(f"Warnings: {len(warnings)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())