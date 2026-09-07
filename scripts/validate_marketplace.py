"""Validate installed snapshot, indexes and provenance without network or mutation."""
import argparse
import json
from pathlib import Path
from release_support import validate_marketplace

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        print(json.dumps(validate_marketplace(args.root), ensure_ascii=False, indent=2))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Marketplace validation failed: {exc}\n")
