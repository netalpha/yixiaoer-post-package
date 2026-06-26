#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


PLATFORMS = {
    "douyin": "抖音",
    "kuaishou": "快手",
    "xiaohongshu": "小红书",
}

VIDEO_NAMES = ("main.mp4", "main.mov")
COVER_NAMES = ("main.jpg", "main.jpeg", "main.png", "main.webp")


def first_existing(folder: Path, names: tuple[str, ...]) -> str | None:
    for name in names:
        candidate = folder / name
        if candidate.is_file():
            return str(candidate)
    return None


def main():
    parser = argparse.ArgumentParser(description="Inspect a Yixiaoer post package.")
    parser.add_argument("package_root", help="Package root folder")
    parser.add_argument("--json", action="store_true", help="Print JSON report")
    args = parser.parse_args()

    root = Path(args.package_root).expanduser().resolve()
    yixiaoer_dir = root / "yixiaoer"
    config_path = yixiaoer_dir / "config.json"
    notes_path = yixiaoer_dir / "notes.md"
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        errors.append(f"package root not found: {root}")
    if not (root / "asset").is_dir():
        warnings.append("asset/ folder is missing")
    if not yixiaoer_dir.is_dir():
        errors.append("yixiaoer/ folder is missing")
    if not config_path.is_file():
        errors.append("yixiaoer/config.json is missing")
    if not notes_path.is_file():
        warnings.append("yixiaoer/notes.md is missing")

    config = {}
    if config_path.is_file():
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid config.json: {exc}")

    enabled = config.get("enabledPlatforms", [])
    if not isinstance(enabled, list):
        errors.append("enabledPlatforms must be a list")
        enabled = []

    unknown = [key for key in enabled if key not in PLATFORMS]
    if unknown:
        errors.append(f"unknown enabled platform key(s): {', '.join(unknown)}")

    platform_reports = []
    for key in enabled:
        if key not in PLATFORMS:
            continue
        platform_dir = yixiaoer_dir / key
        video = first_existing(platform_dir / "video", VIDEO_NAMES)
        cover = first_existing(platform_dir / "cover", COVER_NAMES)
        item = {
            "key": key,
            "name": PLATFORMS[key],
            "platformDir": str(platform_dir),
            "video": video,
            "cover": cover,
            "ready": bool(video and cover),
        }
        if not platform_dir.is_dir():
            errors.append(f"{key}: platform folder missing")
        if not video:
            errors.append(f"{key}: missing video/main.mp4 or video/main.mov")
        if not cover:
            errors.append(f"{key}: missing cover/main.jpg|jpeg|png|webp")
        platform_reports.append(item)

    report = {
        "ok": not errors,
        "packageRoot": str(root),
        "config": str(config_path),
        "notes": str(notes_path),
        "enabledPlatforms": enabled,
        "platforms": platform_reports,
        "errors": errors,
        "warnings": warnings,
    }

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        status = "OK" if report["ok"] else "FAILED"
        print(f"Package inspection: {status}")
        print(f"Root: {root}")
        print(f"Enabled: {', '.join(enabled) if enabled else '(none)'}")
        for item in platform_reports:
            ready = "ready" if item["ready"] else "not ready"
            print(f"- {item['key']} ({item['name']}): {ready}")
            print(f"  video: {item['video'] or 'MISSING'}")
            print(f"  cover: {item['cover'] or 'MISSING'}")
        for warning in warnings:
            print(f"Warning: {warning}")
        for error in errors:
            print(f"Error: {error}")

    raise SystemExit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
