"""Publish an original short scene using Python 3.13's standard library."""
import os
from pathlib import Path

TEXT = (
    "Your back rests against a redwood. "
    "Rain passes from branch to branch, far overhead. "
    "The tree was shelter before this path was here. "
    "By the time a drop reaches the moss beside your hand, you are asleep. "
    "The rest of the rain has all night."
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
