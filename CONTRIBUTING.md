# Contributing to Rebuild Civilization

Thank you for contributing to Rebuild Civilization.

The project aims to build a structured and verifiable knowledge base for the reconstruction of technologies, materials, processes, tools and systems.

Contributions may include:

- new knowledge entities;
- improvements to existing entities;
- documentation;
- sources;
- translations;
- corrections;
- validation tools;
- scripts and automation;
- diagrams and other supporting assets.

Before contributing, read:

- [README.md](README.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [DATA-MODEL.md](DATA-MODEL.md)

These documents define the purpose, architecture and canonical data model of the project.

---

## 1. General principles

Contributions should follow these principles:

- preserve canonical identifiers;
- keep structured data machine-readable;
- do not duplicate canonical entities;
- separate human-readable documentation from canonical structured data;
- use reliable and independent sources;
- clearly indicate uncertainty;
- preserve multilingual consistency;
- prefer incremental and reviewable changes.

Do not make unrelated structural changes in the same contribution.

---

## 2. Types of contributions

The main contribution types are:

- knowledge entities;
- documentation;
- source records;
- translations;
- corrections;
- categories;
- schemas;
- templates;
- scripts;
- validation and automation;
- diagrams and assets.

Each contribution must be placed in the appropriate repository location defined by `ARCHITECTURE.md`.

---

## 3. Adding or modifying a knowledge entity

Canonical knowledge entities currently include:

- `technology`
- `material`
- `process`
- `tool`
- `system`

When creating a new entity:

1. verify that the entity does not already exist;
2. select the appropriate entity type;
3. use the corresponding template;
4. assign a stable canonical ID;
5. place the file in the correct `knowledge/` directory;
6. assign one or more valid categories;
7. assign the appropriate reconstruction phase;
8. add source references;
9. add dependencies and relationships where applicable;
10. indicate the correct evidence and completeness status.

Example locations:

```text
knowledge/technologies/<id>.yaml
knowledge/materials/<id>.yaml
knowledge/processes/<id>.yaml
knowledge/tools/<id>.yaml
knowledge/systems/<id>.yaml
```

The filename should normally match the canonical ID.

---

## 4. Canonical IDs

Canonical IDs must be:

- unique;
- stable;
- language-independent;
- lowercase;
- written in English;
- composed of letters, numbers and hyphens.

Examples:

- `copper-smelting`
- `charcoal-production`
- `mechanical-lathe`
- `water-filtration`

Do not use:

- spaces;
- translated IDs;
- temporary names;
- file paths;
- language prefixes.

Do not change an existing canonical ID unless all references are updated consistently.

---

## 5. Sources and evidence

Factual information should normally be supported by at least two independent reliable sources.

Different URLs do not automatically mean independent sources.

When only one reliable independent source is available:

- use the appropriate evidence status;
- clearly document the limitation.

Do not present uncertain information as established fact.

When reliable sources disagree:

- preserve the disagreement;
- use the appropriate evidence status;
- explain the uncertainty where necessary.

Source records and source references must follow the project data model.

---

## 6. Categories

Categories are defined in:

`knowledge/categories/categories.yaml`

Before creating a new category:

- verify whether an existing category is suitable;
- avoid overly specific categories;
- avoid categories that duplicate entity types;
- avoid categories based only on reconstruction phase;
- assign a parent category where appropriate.

Categories classify knowledge.

They do not define repository location or reconstruction phase.

---

## 7. Reconstruction phases

Canonical reconstruction phases are defined in:

`knowledge/schemas/phases.yaml`

Do not invent phase IDs.

Phases are approximate estimates of when an entity could realistically become reproducible within the project scenario.

They are not guarantees or strict chronological requirements.

Use:

- `expected` for the primary estimated phase;
- `earliest_plausible` for the earliest plausible reconstruction phase;
- `latest_plausible` when a later plausible boundary is useful.

---

## 8. Multilingual content

The initial project languages are:

- Italian: `it`
- English: `en`

Canonical IDs and machine-readable references must remain language-independent.

Example:

```yaml
name:
  it: Fusione del rame
  en: Copper smelting
```

Translations should preserve the meaning of the canonical entity.

Do not create separate canonical entities merely because a translation exists.

If a translation is incomplete, do not invent information.

---

## 9. Documentation

Human-readable documentation is stored in `docs/`.

Documentation is organized by:

- language;
- reconstruction phase.

Documentation should explain knowledge for human readers.

Canonical structured knowledge should remain in `knowledge/`.

Documentation may reference canonical entity IDs where useful.

Do not duplicate large structured datasets inside Markdown documents when the canonical YAML entity already exists.

---

## 10. Templates

Use the appropriate template when creating new content.

Templates are starting structures.

They do not override:

- `ARCHITECTURE.md`;
- `DATA-MODEL.md`;
- controlled values defined in `knowledge/schemas/`;
- canonical categories.

If a template is changed, consider whether the corresponding data model and validation rules must also be updated.

---

## 11. Unknown and uncertain information

Use project conventions for incomplete information.

In general:

- use `null` for an unknown or intentionally unset scalar value;
- use `[]` for a known empty list;
- use `""` only for intentionally empty string fields retained for structural consistency.

Do not use placeholders such as:

- `TBD`
- `N/A`
- `???`
- `unknown`

when a structured value or explicit uncertainty status can be used instead.

Explain important uncertainty in the appropriate notes or documentation fields.

---

## 12. Validation

Before submitting a contribution:

- verify that YAML files are syntactically valid;
- run the project validator when available;
- verify canonical IDs;
- verify categories;
- verify phase IDs;
- verify evidence statuses;
- verify source references;
- verify dependency references;
- verify that files are placed in the correct directories.

A contribution should not introduce broken references or duplicate canonical IDs.

---

## 13. Small and focused changes

Prefer small, focused contributions.

A single contribution should normally address one logical change, for example:

- adding one technology;
- correcting one entity;
- adding a category;
- improving one template;
- adding a validation rule.

Avoid combining unrelated changes unless they are required for consistency.

---

## 14. Updating the data model

When changing the data model:

- identify all affected entity types;
- update the relevant templates;
- update `DATA-MODEL.md`;
- update controlled vocabularies if necessary;
- update the validator;
- consider existing data and backward compatibility.

Do not silently change the meaning of an existing field.

---

## 15. Final checklist

Before submitting a contribution, check:

- [ ] The contribution belongs to the correct repository location.
- [ ] Canonical IDs are unique and valid.
- [ ] The entity type is correct.
- [ ] Categories exist and are appropriate.
- [ ] Phase IDs are valid.
- [ ] Evidence and completeness statuses are valid.
- [ ] Sources are referenced correctly.
- [ ] Dependencies reference existing canonical IDs.
- [ ] YAML is syntactically valid.
- [ ] Multilingual fields are consistent.
- [ ] Uncertainty is clearly represented.
- [ ] No unrelated files were modified.

Thank you for helping build a verifiable and reusable knowledge base for Rebuild Civilization.
