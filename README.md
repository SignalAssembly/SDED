# SDED

Substantive-Description Eponym Deprecation began as an open, community-driven protocol for descriptive naming. The 2.0 revision extends its method to self-documenting terminology in music, philosophy, and the arts and humanities.

The historical project name and acronym are retained for continuity. The expanded scope does not imply that every eponym, cultural name, metaphor, or short symbol should be replaced.

## Current revision

- [Vocabulary index PDF](output/pdf/SDED-2.0-vocabulary.pdf)
- [Complete specification and vocabulary PDF](output/pdf/SDED-2.0.pdf)
- [Complete Markdown edition](SDED-2.0.md)
- [Compact vocabulary in Markdown](vocabulary/SDED-2.0-vocabulary.md)
- [Alphabetical historical-name lookup](vocabulary/HISTORICAL-NAME-LOOKUP.md)
- [Entry-by-entry dates and source notes](research/DATING.md)
- [Framework and case-study paper](paper/SDED-2.0.md)
- [Contribution rules](CONTRIBUTING.md)
- [Machine-readable example records](data/examples.json)
- [Historical reconstruction and source limits](research/HISTORY.md)
- [Publication status](PUBLICATION.md)

The reference restores 438 mappings from the latest prior library and 258 additional earlier mappings, then adds 85 new proposed name pairs. The compact index appears before the extended paper in the full edition. The paper is a conceptual framework and research protocol. Proposed descriptors are explicitly distinguished from established terms and empirically validated recommendations.

## Historical attribution

Default: `Descriptive name ("Historical name", est. YYYY)`.

The trademark symbol is acceptable but optional: `Descriptive name ("Historical name"™, est. YYYY)`. Its absence never prevents participation or conformance. The marker is a stylistic element, not a concept identifier or evidence of trademark status. Every indexed entry has a date, approximate period, or documented range; `by 1872` is an upper bound, not an invention claim. All 85 additions have source notes and 14 inherited records have explicit date corrections. Other inherited dates retain their recorded verification status. The build rejects blank or unknown dates and missing date evidence for additions.

## Earlier work

Published v1.1: [10.5281/zenodo.17418489](https://doi.org/10.5281/zenodo.17418489), issued October 22, 2025. Version-series DOI: [10.5281/zenodo.17418488](https://doi.org/10.5281/zenodo.17418488).

The repository also preserves v1.2 development artifacts. Historical PDFs are archival and do not specify the 2.0 rules. The 2.0 revision does not revalidate every entry in the earlier vocabulary.

Text: CC BY 4.0, continuing the earlier project's license.

## Rebuilding

Run `python3 scripts/build_vocabulary.py` with pypdf installed to recover the prior mappings, render the compact index, and assemble `SDED-2.0.md`. Run `python3 scripts/build_data.py` to export the eighty eight-field audit proposals and eight chord-quality records. Run `python3 scripts/build_pdf.py` with ReportLab installed to typeset the complete edition; add `--vocabulary-only` for the separate reference PDF. The PDF builder uses Lato faces in `SDED_FONT_DIR` (default `/Library/Fonts`) and a Unicode fallback font selected by `SDED_FALLBACK_FONT`. It checks glyph coverage before writing the PDF. It adds a linked contents page and cited-source index.

After rebuilding both PDFs, run `python3 scripts/package_release.py` to package the public sources, including the historical recovery inputs, and refresh the artifact checksums.

The example data are proposals, not an approved replacement dictionary. Audit IDs identify discussion records; the separately scoped chord-quality IDs identify the construction types used in the demonstration.
