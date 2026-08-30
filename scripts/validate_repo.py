#!/usr/bin/env python3
"""Validate the required course-wiki directory structure."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md", "course.yaml", "study.yaml", "README.md",
    "sources/inbox", "sources/official", "sources/external", "sources/extracted", "sources/catalog.yaml",
    "notes/inbox", "notes/processed", "wiki/README.md", "wiki/index.md", "wiki/glossary.md", "wiki/questions.md", "wiki/conflicts.md", "wiki/topics",
    "practice", "labs",
    ".agents/skills/ingest-material/SKILL.md", ".agents/skills/study/SKILL.md", ".agents/skills/audit-wiki/SKILL.md",
    "scripts/extract_pdf.py", "scripts/validate_repo.py",
]


def main() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        print("Missing required paths:")
        print(*missing, sep="\n")
        sys.exit(1)
    print("Repository structure is valid.")


if __name__ == "__main__":
    main()
