# Templates

This directory contains the canonical templates used to create new
project entities and documents.

## Structure

```text
templates/
├── README.md
├── knowledge/
│   ├── technology.yaml
│   ├── material.yaml
│   ├── process.yaml
│   ├── tool.yaml
│   └── system.yaml
├── sources/
│   └── source.yaml
└── docs/
    └── material.md
```

The canonical documentation pattern is one Markdown file per analyzed item, stored inside the destination phase folder.

Example:

```text
docs/
├── it/
│   ├── 02-2-5-anni/
│   │   ├── charcoal-production.md
│   │   └── kiln-construction.md
│   └── 03-5-15-anni/
│       └── simple-copper-smelting.md
└── en/
    ├── 02-2-5-years/
    │   ├── charcoal-production.md
    │   └── kiln-construction.md
    └── 03-5-15-years/
        └── simple-copper-smelting.md
```

Each file must contain the sections required for the analysis: Material, System, Technology, Tools, Process, and the explicit objective of what is to be achieved.

## Authority

Templates are starting structures and do not override the project architecture
or data model.

The authoritative documents are:

ARCHITECTURE.md — repository structure and architecture.
DATA-MODEL.md — meaning and structure of canonical data.
knowledge/schemas/ — controlled values and reference definitions.
knowledge/categories/categories.yaml — canonical category vocabulary.

Templates must remain consistent with these definitions.
