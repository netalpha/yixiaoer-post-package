#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path


def ignore_noise(_dir, names):
    return {name for name in names if name in {".DS_Store", "__pycache__"}}


def main():
    parser = argparse.ArgumentParser(description="Create a Yixiaoer post package from the bundled template.")
    parser.add_argument("destination", help="Destination package folder to create")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing destination")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    template = skill_dir / "assets" / "template"
    destination = Path(args.destination).expanduser().resolve()

    if not template.exists():
        raise SystemExit(f"template not found: {template}")

    if destination.exists():
        if not args.force:
            raise SystemExit(f"destination already exists: {destination}")
        shutil.rmtree(destination)

    shutil.copytree(template, destination, ignore=ignore_noise)
    print(destination)


if __name__ == "__main__":
    main()
