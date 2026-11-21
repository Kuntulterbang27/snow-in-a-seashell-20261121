"""Publish an original short scene using Python 3.13's standard library."""
import os
from pathlib import Path

TEXT = (
    "High in the mountains, a fossil shell fills with snow. "
    "Once, a warm sea moved here. "
    "All afternoon, snow settles into its curves, one flake at a time."
)


def main():
    if not TEXT.strip() or not 1 <= len(TEXT) <= 280:
        raise ValueError("Entry must contain 1-280 Unicode code points")
    directory = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "entry.txt"
    path.write_bytes(TEXT.encode("utf-8"))
    path.chmod(0o644)


if __name__ == "__main__":
    main()
