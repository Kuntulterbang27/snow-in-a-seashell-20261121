"""Publish an original short scene using Python 3.13's standard library."""
import os
from pathlib import Path

TEXT = (
    "You are half asleep in a redwood's shade. "
    "Rain stays high in the branches, then finds its way down, leaf to leaf. "
    "The tree was old before this path was made. "
    "A drop lands beside your hand. Another is still on its way."
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
