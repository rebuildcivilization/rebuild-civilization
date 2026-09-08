# Rebuild Civilization — Project Architecture

## 1. Purpose

Rebuild Civilization is an open knowledge project that describes how technological and social capabilities could be rebuilt after a severe disruption or collapse of modern technological civilization.

The project is not intended to be a conventional encyclopedia.

Its primary purpose is to answer:

> What must be rebuilt first, what depends on what, and how could a society progressively recover technological capabilities starting from a very low technological base?

The project therefore combines:

- Human-readable documentation
- Structured knowledge
- Technological dependencies
- Reconstruction phases
- Categories
- Source verification
- Multilingual documentation

---

## 2. Core concepts

The project separates five concepts that must not be confused.

### Phase

When a capability could realistically become part of the reconstruction process.

### Category

What kind of capability, knowledge, technology, material or process it is.

### Dependency

What must already exist before a capability can be reproduced.

### Knowledge

The canonical reusable information describing technologies, materials, processes, tools and systems.

### Documentation

Human-readable explanations that organize and present the knowledge.

A document's location, category and phase are separate concepts.

---

## 3. Reconstruction phases

The primary organization of `docs/` is chronological.

The phases represent approximate reconstruction periods, not guaranteed deadlines.

### Phase 0 — Survival

**Primary objective: survival and manage first emergencies.**

This phase defines the project before reconstruction activities begin.
IS split on two level:
 - 0A — Immediate Survival
 - 0B — Stabilization

Typical subjects include:

- Water
- Food
- Health
- Basic tools
- Fire
- Food preservation

Italian directory: `docs/it/00-soprevvivenza/`

English directory: `docs/en/00-survival/`

### Phase 1 — 0–2 years

**Primary objective: stabilization and preservation of knowledge.**

Typical subjects include:s

- Food
- Shelter
- Health
- Sanitation
- Basic tools
- Food preservation
- Initial organization
- Protection of surviving knowledge and equipment

Italian directory: `docs/it/01-0-2-anni/`

English directory: `docs/en/01-0-2-years/`

### Phase 2 — 2–5 years

**Primary objective: basic self-sufficiency and local production.**

Typical subjects include:

- Agriculture
- Animal husbandry
- Ceramics
- Glass
- Charcoal
- Basic metallurgy
- Basic mechanical production
- Simple energy systems
- Workshops
- Storage
- Local transport

Italian directory: `docs/it/02-2-5-anni/`

English directory: `docs/en/02-2-5-years/`

### Phase 3 — 5–15 years

**Primary objective: initial industrialization.**

Typical subjects include:

- Improved metallurgy
- Machine tools
- Mechanical power
- Steam technology
- Electricity
- Chemical processes
- Mining
- Industrial materials
- Communications
- Larger-scale manufacturing

Italian directory: `docs/it/03-5-15-anni/`

English directory: `docs/en/03-5-15-years/`

### Phase 4 — 15–30 years

**Primary objective: advanced industrial infrastructure.**

Typical subjects include:

- Electrical grids
- Advanced machine tools
- Industrial chemistry
- Telecommunications
- Precision manufacturing
- Advanced materials
- Industrial automation
- Complex transportation systems

Italian directory: `docs/it/04-15-30-anni/`

English directory: `docs/en/04-15-30-years/`

### Phase 5 — 30–50 years

**Primary objective: reconstruction of advanced technological infrastructure.**

Typical subjects include:

- Electronics
- Computing
- Semiconductor technology
- Advanced telecommunications
- Automation
- Digital networks
- Advanced scientific instrumentation

Italian directory: `docs/it/05-30-50-anni/`

English directory: `docs/en/05-30-50-years/`

### Phase 6 — 50+ years

**Primary objective: recovery and further development of highly advanced technologies.**

Examples may include:

- Advanced semiconductor manufacturing
- Advanced computing
- Sophisticated robotics
- Aerospace
- Advanced biotechnology
- High-performance materials
- Technologies requiring complex industrial ecosystems

Italian directory: `docs/it/06-oltre-50-anni/`

English directory: `docs/en/06-50-plus-years/`

---

## 4. Important rule about time estimates

The phase assigned to a technology represents an approximate reconstruction scenario.

It is **not** a guaranteed chronological prediction.

Actual reconstruction time depends on:

- Surviving population
- Available skills
- Surviving infrastructure
- Surviving machinery
- Available raw materials
- Energy availability
- Environmental conditions
- Geographic location
- Access to surviving technology
- Institutional and social organization

A technology may therefore have:

- An expected phase
- An earliest plausible phase
- Prerequisites that may move it to a later phase

Phase numbers must not be treated as absolute technological laws.

---

## 5. Repository structure

The repository uses the following top-level structure:

```text
/
├── README.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
│
├── docs/
│   ├── it/
│   └── en/
│
├── knowledge/
│   ├── technologies/
│   ├── materials/
│   ├── processes/
│   ├── tools/
│   ├── systems/
│   ├── categories/
│   │   └── categories.yaml
│   └── schemas/
│       ├── phases.yaml
│       ├── evidence-statuses.yaml
│       └── completeness-statuses.yaml
│
├── sources/
│   └── catalog/
│
├── templates/
│
├── assets/
│   ├── images/
│   ├── diagrams/
│   └── maps/
│
├── scripts/
│
└── .github/
```

The repository structure may evolve, but new top-level directories should not be introduced without a clear architectural reason.

---

## 6. Documentation

`docs/` contains human-readable documentation.

Documentation is organized primarily by:

1. Language
2. Reconstruction phase

The Italian documentation structure is:

```text
docs/
└── it/
    ├── 00-sopravvivenza/
    |   ├── 0A — Sopravvivenza immediata 
    |   └── 0B — Stabilizzazione         
    ├── 01-0-2-anni/
    ├── 02-2-5-anni/
    ├── 03-5-15-anni/
    ├── 04-15-30-anni/
    ├── 05-30-50-anni/
    └── 06-oltre-50-anni/
```

The English documentation structure is:

```text
docs/
└── en/
    ├── 00-survival/
    |   ├── 0A — Immediate Survival 
    |   └── 0B — Stabilization         
    ├── 01-0-2-years/
    ├── 02-2-5-years/
    ├── 03-5-15-years/
    ├── 04-15-30-years/
    ├── 05-30-50-years/
    └── 06-50-plus-years/
```

Directory names may be translated.

The underlying phase concept and phase identifier must remain language-independent.

---

## 7. Structured knowledge

`knowledge/` contains canonical, machine-readable descriptions.

It is independent from the language of the documentation.

The main knowledge types are:

- `technologies/`
- `materials/`
- `processes/`
- `tools/`
- `systems/`
- `categories/`

Example:

```text
knowledge/
└── technologies/
    └── copper-smelting.yaml
```

The same canonical technology, material, process or system must not be duplicated for each language.

### Schemas and controlled vocabularies

`knowledge/schemas/` contains controlled values and reusable reference
definitions used by canonical knowledge entities.

Initial schema files include:

- `phases.yaml`
- `evidence-statuses.yaml`
- `completeness-statuses.yaml`

The directory does not contain knowledge entities.

It defines values and structures referenced by those entities.

### Categories

`knowledge/categories/` contains the canonical project taxonomy.

Initial category definitions are stored in:

`knowledge/categories/categories.yaml`

Categories classify knowledge independently from reconstruction phases
and repository location.

---

## 8. Language-independent identifiers

All machine-readable identifiers must use English.

Example:

```yaml
id: copper-smelting
```

Categories also use stable English identifiers:

```yaml
categories:
  - metallurgy
  - materials
  - manufacturing
```

Dependencies reference canonical identifiers:

```yaml
prerequisites:
  technologies:
    - charcoal-production
    - furnace
  materials:
    - copper-ore
  tools:
    - hammer
```

Identifiers must remain stable across translations.

---

## 9. Categories

Categories classify knowledge independently from reconstruction phases.

A technology, process or other knowledge entity may belong to multiple categories.

Example:

```yaml
categories:
  - metallurgy
  - materials
  - manufacturing
```

Categories must be:

- Reusable
- Stable
- Language-independent
- Lowercase
- Expressed as identifiers

Do not create a new category when an existing category is sufficient.

The canonical category definitions are maintained in:

`knowledge/categories/`

A document's directory, its phase and its categories are separate concepts.

---

## 10. Dependencies

Dependencies are a core component of the project.

A technology should explicitly identify, when applicable:

- Required technologies
- Required materials
- Required tools
- Required processes
- Required knowledge
- Required energy
- Required infrastructure

Example:

```yaml
prerequisites:
  technologies:
    - charcoal-production
    - furnace
  materials:
    - copper-ore
  tools:
    - hammer
```

Dependencies should be explicit rather than hidden only in prose.

Circular dependencies should be avoided.

If a circular dependency represents a genuine bootstrap problem, it must be explicitly documented.

---

## 11. Sources and evidence

Every factual document should normally contain at least **two independent sources**.

The preferred model is:

1. A primary, academic, scientific, institutional or technical source
2. An independent second source for confirmation, comparison or context

Two pages that simply reproduce the same original source do not count as independent sources.

If only one reliable source is available, the document may still be created, but it must explicitly declare this limitation.

Example notice:

> **Source limitation:** This document currently relies on only one independent source. Additional verification is required.

If no reliable source exists, the information must not be presented as verified fact.

Possible evidence statuses include:

- `verified`
- `partially_verified`
- `single_source`
- `conflicting_sources`
- `insufficient_sources`
- `unsourced`

When reliable sources conflict, the disagreement must be explicitly documented.

---

## 12. Source catalog

Sources should be represented in the centralized source catalog:

`sources/catalog/`

Each source should have a stable identifier.

Example:

```yaml
id: source-001
title: Example Technical Manual
author: Example Organization
year: 1985
language: en
type: technical-manual
url: https://example.org/
```

Knowledge documents should reference source identifiers rather than unnecessarily duplicating complete bibliographic records.

---

## 13. Multilingual documentation

The project is multilingual.

Initial supported languages are:

- Italian: `it`
- English: `en`

Additional languages may be added later.

Machine-readable identifiers, YAML keys, category IDs and dependency IDs must remain language-independent.

Translations must preserve the meaning of the canonical content.

Translations must not introduce new technical claims without appropriate sources.

A missing translation is preferable to an inaccurate translation.

---

## 14. Safety and uncertainty

The project should clearly distinguish between:

- Established fact
- Experimentally demonstrated procedure
- Historical reconstruction
- Engineering estimate
- Hypothesis
- Uncertain information

Uncertain information must not be presented as established fact.

Dangerous procedures should be clearly identified and documented responsibly.

---

## 15. Long-term principles

The project favors:

- Open formats
- Simple formats
- Reproducible processes
- Explicit dependencies
- Stable identifiers
- Source-backed claims
- Human-readable documentation
- Machine-readable data

The project should avoid unnecessary complexity.

The repository should remain understandable and usable decades from now, even if specific software platforms, tools or AI systems no longer exist.
