# Course Wiki Template

A local, Git-native workspace for turning course sources into a traceable,
concept-oriented study wiki.

The V1 workflow is:

1. `ingest-material` preserves and catalogs sources, extracts searchable text, and synthesizes supported wiki topics.
2. `study` uses the compiled wiki as a read-only tutoring layer.
3. `audit-wiki` combines deterministic validation with semantic review.

Practical assignments are cataloged separately from teaching sources. Upload
them to `sources/inbox/` for ingestion, or place them directly in
`sources/practical-assignment/`. Their originals remain unchanged, their catalog
type is `practical_assignment`, and searchable extracts use `PA-NNN` IDs:

```yaml
sources:
  - id: PA-001
    title: Practical assignment 1
    type: practical_assignment
    path: practical-assignment/assignment-1.pdf
    extracted: extracted/PA-001.md
```

Ingestion preserves the assignment's questions and requirements without
generating wiki content from it. Tutoring uses PAs as task context and the
wiki and teaching sources to explain and solve them.

Install the script dependencies with:

```bash
python -m pip install -r requirements.txt
```

Searchable Markdown extraction is built in for PDF, DOCX, and PPTX sources.
PDF extracts preserve page boundaries; PowerPoint extracts preserve slide
boundaries. Office extraction includes textual document content, tables, and
PowerPoint speaker notes, and warns when visual or unsupported content requires
inspection of the immutable original.
