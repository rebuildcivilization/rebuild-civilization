# Rebuild Civilization — Data Model

## 1. Purpose

This document defines the canonical structured data model used by the project.

It specifies:

- common fields shared by knowledge entities;
- entity types;
- identifier rules;
- phase representation;
- category representation;
- source references;
- evidence and completeness status;
- relationships and dependencies;
- rules for unknown or incomplete information.

`ARCHITECTURE.md` defines where data belongs in the repository.

`DATA-MODEL.md` defines what the structured data means.

---

## 2. Canonical entity types

The initial canonical knowledge entities are:

- `technology`
- `material`
- `process`
- `tool`
- `system`

Additional entity types may be introduced only when the existing model is insufficient.

Every canonical knowledge entity has one stable identifier and must not be duplicated by language.

---

## 3. Common entity model

All canonical knowledge entities should use the following common structure where applicable:

```yaml
id: ""
type: ""

name:
  it: ""
  en: ""

summary:
  it: ""
  en: ""

status:
  evidence: insufficient_sources
  completeness: draft

phase:
  expected: null
  earliest_plausible: null
  latest_plausible: null

categories: []

sources: []

notes:
  it: ""
  en: ""

metadata:
  created: ""
  updated: ""
```

Entity-specific fields are added after the common fields.

Not every common field is necessarily applicable to every entity type.

Required fields defined by a specific entity template must not be silently omitted.

---

## 4. Canonical identifiers

The id field is the canonical identifier of an entity.

Canonical IDs must be:

globally unique;
stable;
language-independent;
written in English;
lowercase;
composed only of letters, numbers and hyphens;
descriptive but not unnecessarily long.

Examples:

copper-smelting
copper-ore
charcoal-production
water-filtration
mechanical-lathe

Do not use:

spaces;
translated IDs;
temporary numeric names;
file paths as IDs;
language prefixes such as it- or en-.

Once an ID is referenced by other entities, it should not be changed unless all references are migrated together.

---

## 5. Entity type

The type field identifies the canonical entity type.

Initial allowed values are:

technology
material
process
tool
system

The type must match:

the entity template;
the directory where the entity is stored;
the semantic nature of the entity.

Examples:

id: copper-smelting
type: technology
id: copper-ore
type: material
6. Multilingual fields

Human-readable structured content may be stored by language.

Initial supported language keys are:

it
en

Example:
name:
  it: Fusione del rame
  en: Copper smelting

A missing translation may temporarily be represented by an empty value.

Translations must not receive different canonical IDs.

Additional language keys may be added later without changing the entity structure.

Machine-readable keys, IDs, category IDs, phase IDs and dependency IDs must remain language-independent.

---

## 7. Status model

### 7.1 Evidence status

The status.evidence value must exist in:

knowledge/schemas/evidence-statuses.yaml

Initial allowed values are:

verified
partially_verified
single_source
conflicting_sources
insufficient_sources
unsourced

The status describes the quality and sufficiency of evidence for the entity as a whole.

If only part of an entity is uncertain, use partially_verified and document the uncertainty in notes or in the related human-readable documentation.

### 7.2 Completeness status

Initial allowed values are:
 - draft
 - in_progress
  - complete
  - needs_review
  - deprecated

If the list becomes more complex, it should be moved to a dedicated schema file. 

---

## 8. Reconstruction phases

The phase object represents the approximate reconstruction period in which an entity is expected to become realistically reproducible.

Phase values must reference the canonical definitions in:

knowledge/schemas/phases.yaml

Example:

phase:
  expected: phase-02
  earliest_plausible: phase-01
  latest_plausible: null

Rules:

expected should normally be present for reconstructible entities;
earliest_plausible must not be later than expected;
latest_plausible, when used, must not be earlier than expected;
phases represent approximate reconstruction scenarios, not guarantees.

Do not use translated documentation directory names as canonical phase identifiers.

---

## 9. Categories

The categories field is a list of canonical category IDs.

Example:

categories:
  - metallurgy
  - manufacturing

Every category ID must exist in:

knowledge/categories/categories.yaml

Categories are:

independent from repository location;
independent from reconstruction phase;
reusable;
language-independent.

An entity may belong to multiple categories.

Do not create a new category merely because a concept is located in a different documentation phase.

---

## 10. Source references

The sources field contains references to source IDs stored in:

sources/catalog/

Example:

sources:
  - source-001
  - source-002

Source records contain bibliographic, access and reliability information.

Knowledge entities should reference source IDs rather than duplicate complete bibliographic records.

Every factual entity should normally have at least two independent reliable sources.

If only one independent source exists:

use the single_source evidence status;
document the limitation.

Source independence is defined by the origin of the evidence, not merely by different URLs or publishers.

---

## 11. Dependencies and references

Dependencies must reference canonical entity IDs.

Do not use:

filenames;
translated names;
relative paths;
duplicated descriptions when a canonical entity ID exists.

Example:

prerequisites:
  technologies:
    - charcoal-production
  materials:
    - copper-ore
    - charcoal
  tools:
    - furnace

A dependency should be placed in the most appropriate semantic relationship.

For example:

a material required to perform a process belongs in materials;
a required tool belongs in tools;
a prerequisite technology belongs in technologies.

Do not use a generic dependency list when a typed relationship is available.

---

## 12. Entity relationships

Relationships may include:

prerequisites;
inputs;
outputs;
related entities;
substitutes;
components;
subsystems;
alternatives.

Relationship fields should contain canonical IDs.

The relationship direction must be clear from the field name.

Examples:

inputs:
  materials:
    - copper-ore
outputs:
  materials:
    - copper
related:
  technologies:
    - bronze-production

---

## 13. Unknown and not applicable values

Use the following conventions:

[] for a known empty list;
null for an unknown or intentionally unset scalar value;
"" for an intentionally empty string field that is retained for structural consistency;
omit an optional field only when the relevant template explicitly allows omission.

Do not use placeholder values such as:

unknown-value
TBD
N/A
???

Use notes to explain uncertainty when necessary.

---

## 14. Metadata

Every canonical entity should contain:

metadata:
  created: ""
  updated: ""

Dates use ISO 8601 format:

YYYY-MM-DD

Example:

metadata:
  created: "2026-08-24"
  updated: "2026-08-24"

The updated date must change when the entity is materially modified.

Metadata must not be used to encode entity meaning.

---

## 15. File and entity correspondence

A canonical entity should normally have one primary YAML file.

Recommended examples:

knowledge/technologies/copper-smelting.yaml
knowledge/materials/copper-ore.yaml
knowledge/processes/charcoal-production.yaml
knowledge/tools/mechanical-lathe.yaml
knowledge/systems/electrical-grid.yaml

The filename should normally match the canonical ID:

<id>.yaml

---

## 16. Controlled vocabularies

Controlled values and reusable definitions are stored in:

knowledge/schemas/
├── phases.yaml
└── evidence-statuses.yaml

Canonical categories are stored separately:

knowledge/categories/categories.yaml

The distinction is:

schemas/ defines controlled values and reusable reference definitions;
categories/ defines the taxonomy used to classify knowledge.

---

## 17. Validation rules

Structured data should be validated for:

valid YAML syntax;
unique canonical IDs;
valid entity type;
correct repository location;
valid phase IDs;
valid category IDs;
valid evidence statuses;
existing source references;
existing dependency references;
absence of accidental duplicate entities;
phase consistency where applicable.

Validation should eventually be automated through scripts or CI.

---

## 18. Evolution of the model

The data model may evolve.

When adding a field:

determine whether it applies to all entity types or only one;
avoid duplicating the same concept under different names;
update the relevant template;
update this document;
consider migration and backward compatibility;
update validation rules if applicable.

Do not change the meaning of an existing field without documenting the migration.

---

## 19. Authority

For structured data:

ARCHITECTURE.md defines where data belongs.
DATA-MODEL.md defines what the data means.
templates/ defines the canonical starting structure for new entities.
knowledge/schemas/ defines controlled values and reusable reference definitions.
knowledge/categories/categories.yaml defines the canonical category vocabulary.

If these documents conflict, the conflict must be resolved explicitly before new structured data is created.



