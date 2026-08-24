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
└── documents/
    ├── technology.md
    ├── material.md
    ├── process.md
    ├── tool.md
    └── system.md

Authority

Templates are starting structures and do not override the project architecture
or data model.

The authoritative documents are:

ARCHITECTURE.md — repository structure and architecture.
DATA-MODEL.md — meaning and structure of canonical data.
knowledge/schemas/ — controlled values and reference definitions.
knowledge/categories/categories.yaml — canonical category vocabulary.

Templates must remain consistent with these definitions.
