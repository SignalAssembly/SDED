"""Package the public sources and checksum the release artifacts."""
import hashlib
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ".zenodo.json", ".gitattributes", ".gitignore", "README.md",
    "PUBLICATION.md", "CONTRIBUTING.md", "CHANGELOG.md", "SDED-2.0.md",
    "SDED_metadata.json", "v1.2_metadata.json",
    "build_sded_v1_2_RevisionB_full.py", "expanded_libraries.py",
    "build_sded_v1_2_full.py",
    "SDED v1.2_ Specification and Approved Vocabulary Set 1.pdf",
    "SDED_Protocol_Specification_v1.2.pdf", "SDED_v1_2_RevisionB_FULL.pdf",
    "SDED_v1_2_full.pdf", "paper/SDED-2.0.md",
    "vocabulary/SDED-2.0-vocabulary.md", "vocabulary/HISTORICAL-NAME-LOOKUP.md",
    "data/inherited-vocabulary.json", "data/new-vocabulary.tsv",
    "data/new-vocabulary.json", "data/examples.json", "data/chord-quality-matrix.json",
    "research/HISTORY.md", "research/VERIFICATION.md",
    "scripts/build_vocabulary.py", "scripts/build_pdf.py", "scripts/build_data.py",
    "scripts/package_release.py",
]

archive = ROOT / "output/SDED-2.0-source.zip"
archive.parent.mkdir(exist_ok=True)
for name in SOURCES:
    if not (ROOT / name).is_file():
        raise FileNotFoundError(name)
with ZipFile(archive, "w", ZIP_DEFLATED) as package:
    for name in SOURCES:
        package.write(ROOT / name, "SDED-2.0/" + name)
with ZipFile(archive) as package:
    assert package.testzip() is None
    assert len(package.namelist()) == len(SOURCES)

artifacts = [ROOT / "output/pdf/SDED-2.0.pdf",
             ROOT / "output/pdf/SDED-2.0-vocabulary.pdf", archive]
checksums = [hashlib.sha256(path.read_bytes()).hexdigest() + "  "
             + path.relative_to(ROOT / "output").as_posix() for path in artifacts]
(ROOT / "output/SHA256SUMS.txt").write_text("\n".join(checksums) + "\n")
print(f"Packaged {len(SOURCES)} public source files; checksummed {len(artifacts)} artifacts.")
