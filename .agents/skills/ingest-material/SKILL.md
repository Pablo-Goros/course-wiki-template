---
name: ingest-material
description: Ingest pending course sources into the catalog, searchable extracts, and a traceable concept-oriented wiki. Use when new files in sources/inbox need to be incorporated.
---

# Ingest Material

Transform classifiable files in `sources/inbox/` into preserved evidence and
source-backed wiki knowledge. Work from the repository root. Read `AGENTS.md`,
`course.yaml`, `wiki/index.md`, and `wiki/topic-template.md` before processing
academic content.

## Process the inbox

Inspect every pending file and classify it as:

- `official`: supplied by the course, chair, or instructor.
- `external`: complementary books, papers, documentation, or other outside
  resources.

Use file contents and available provenance, not filename guesses. Leave an
ambiguous file in the inbox and report what evidence is missing.

For each classifiable source:

1. Read `sources/catalog.yaml` and assign the next unused ID for its type:
   `OFF-NNN` or `EXT-NNN`. IDs are stable, independent of filenames, and must
   never be reassigned, recycled, or removed merely because a source changes
   location.
2. Move the original without changing its bytes to `sources/official/` or
   `sources/external/`.
3. Add the minimal catalog record: `id`, `title`, `type`, `path`, and
   `extracted` when an extract exists. Paths are relative to `sources/`.
4. For a PDF, run:

   ```bash
   python scripts/extract_pdf.py sources/<type>/<file>.pdf --output sources/extracted/<SOURCE-ID>.md
   ```

   Extraction is a regenerable retrieval aid, not authority. If important
   information depends on images, diagrams, formulas, tables, or spatial
   layout, inspect the original page when possible and do not infer missing
   meaning from extracted text. For other formats, preserve the original and
   create an ID-named searchable derivative only when the format can be
   converted without academic interpretation.

## Synthesize the wiki

Understand the source before editing topics. Use `wiki/index.md` as the map,
then search topic titles, aliases, synonyms, and equivalent terms. Update an
existing topic when the concept naturally belongs there. Create a new topic
only for a concept that could reasonably support an independent academic
question; never mirror document units such as classes, chapters, or slides.

Follow `wiki/topic-template.md`, adapting optional sections to the concept.
Use the academic language configured in `course.yaml`, lowercase kebab-case
filenames, and aliases for important equivalent names in other languages.
Prefer links over repeated explanations. Maintain meaningful `related` and
`prerequisites` relationships.

Synthesize across sources according to `course.yaml` authority. Trace important
claims with repository citations such as `[OFF-001, p. 12]` or
`[EXT-003, pp. 45-47]`; do not cite general model knowledge as course evidence.
Add exam relevance only when repository evidence supports it, and distinguish
explicit evidence from inference.

Update `wiki/index.md` after topic creation, renaming, or reorganization. Keep
it a concise navigation map rather than a course summary.

## Complete the run

Run `python scripts/validate_repo.py`, inspect the full Git diff, and report:

- sources incorporated;
- topics created and updated;
- unresolved classification or content ambiguities;
- validation problems.

Do not commit or push unless explicitly requested.
