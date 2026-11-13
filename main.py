"""Publish the 13 November 2026 front page for the make.fun news-image-01 bounty.

Copies the bundled ``entry.png`` into the output directory as ``entry.png``,
creating the output directory first if it does not yet exist.
"""

import os
import shutil

ENTRY_NAME = "entry.png"
OUT_DIR = "/output"


def publish(output_dir: str = OUT_DIR) -> str:
    """Copy the entry image into ``output_dir`` and return the destination path."""
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), ENTRY_NAME)
    os.makedirs(output_dir, exist_ok=True)
    dest = os.path.join(output_dir, ENTRY_NAME)
    shutil.copyfile(src, dest)
    return dest


def main() -> None:
    # Honor ENTRY_OUTPUT_DIR so the script can be verified against a temp dir.
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", OUT_DIR)
    print(publish(output_dir))


if __name__ == "__main__":
    main()
