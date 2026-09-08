# SDED

Substantive-Description Eponym Deprecation began as an open, community-driven protocol for descriptive naming. The 2.0 revision extends its method to self-documenting terminology in music, philosophy, and the arts and humanities.

The historical project name and acronym are retained for continuity. The expanded scope does not imply that every eponym, cultural name, metaphor, or short symbol should be replaced.

## Current revision

- [SDED 2.0 manuscript](paper/SDED-2.0.md)
- [PDF reading edition](output/pdf/SDED-2.0.pdf)
- [Contribution rules](CONTRIBUTING.md)
- [Machine-readable example records](data/examples.json)
- [Historical reconstruction and source limits](research/HISTORY.md)
- [Publication status](PUBLICATION.md)

The manuscript is a conceptual framework and research protocol. Proposed descriptors are explicitly distinguished from established terms and empirically validated recommendations.

## Historical attribution

Default: `Descriptive name ("Historical name", est. YYYY)`.

The trademark symbol is acceptable but optional: `Descriptive name ("Historical name"™, est. YYYY)`. Its absence never prevents participation or conformance. The marker is a stylistic element, not a concept identifier or evidence of trademark status. Do not invent establishment dates; record the event being dated and its source.

## Earlier work

Published v1.1: [10.5281/zenodo.17418489](https://doi.org/10.5281/zenodo.17418489), issued October 22, 2025. Version-series DOI: [10.5281/zenodo.17418488](https://doi.org/10.5281/zenodo.17418488).

The repository also preserves v1.2 development artifacts. Historical PDFs are archival and do not specify the 2.0 rules. The 2.0 revision does not revalidate every entry in the earlier vocabulary.

Text: CC BY 4.0, continuing the earlier project's license.

## Rebuilding

Run `python3 scripts/build_data.py` to export the eighty eight-field audit proposals and eight chord-quality records. Run `python3 scripts/build_pdf.py` with ReportLab installed to typeset the manuscript. The PDF builder uses Lato faces in `SDED_FONT_DIR` (default `/Library/Fonts`) and a Unicode fallback font selected by `SDED_FALLBACK_FONT`. It checks glyph coverage before writing the PDF. It adds a linked contents page and cited-source index.

The example data are proposals, not an approved replacement dictionary. Audit IDs identify discussion records; the separately scoped chord-quality IDs identify the construction types used in the demonstration.
