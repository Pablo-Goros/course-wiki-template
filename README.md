# Course Wiki Template

A local, Git-native workspace for turning course sources into a traceable,
concept-oriented study wiki.

The V1 workflow is:

1. `ingest-material` preserves and catalogs sources, extracts searchable text, and synthesizes supported wiki topics.
2. `study` uses the compiled wiki as a read-only tutoring layer.
3. `audit-wiki` combines deterministic validation with semantic review.

Install the script dependencies with:

```bash
python -m pip install -r requirements.txt
```

Searchable Markdown extraction is built in for PDF, DOCX, and PPTX sources.
PDF extracts preserve page boundaries; PowerPoint extracts preserve slide
boundaries. Office extraction includes textual document content, tables, and
PowerPoint speaker notes, and warns when visual or unsupported content requires
inspection of the immutable original.
