#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


PLATFORMS = {
    "douyin": "抖音",
    "kuaishou": "快手",
    "xiaohongshu": "小红书",
}

VIDEO_EXTENSIONS = {".mp4", ".mov"}
COVER_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
IGNORED_NAMES = {"README.md", ".DS_Store"}


def final_files(folder: Path, extensions: set[str]) -> list[Path]:
    if not folder.is_dir():
        return []
    return sorted(
        path
        for path in folder.iterdir()
        if path.is_file()
        and path.name not in IGNORED_NAMES
        and not path.name.startswith(".")
        and path.suffix.lower() in extensions
    )


def main():
    parser = argparse.ArgumentParser(description="Inspect a Yixiaoer post package.")
    parser.add_argument("package_root", help="Package root folder")
    parser.add_argument("--json", action="store_true", help="Print JSON report")
    args = parser.parse_args()

    root = Path(args.package_root).expanduser().resolve()
    yixiaoer_dir = root / "yixiaoer"
    config_path = yixiaoer_dir / "config.json"
    notes_path = yixiaoer_dir / "notes.md"
    simple_config_path = yixiaoer_dir / "简易发布配置.md"
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
        videos = final_files(platform_dir / "video", VIDEO_EXTENSIONS)
        covers = final_files(platform_dir / "cover", COVER_EXTENSIONS)
        video = str(videos[0]) if len(videos) == 1 else None
        cover = str(covers[0]) if len(covers) == 1 else None
        item = {
            "key": key,
            "name": PLATFORMS[key],
            "platformDir": str(platform_dir),
            "video": video,
            "cover": cover,
            "videoCount": len(videos),
            "coverCount": len(covers),
            "videos": [str(path) for path in videos],
            "covers": [str(path) for path in covers],
            "ready": bool(video and cover),
        }
        if not platform_dir.is_dir():
            errors.append(f"{key}: platform folder missing")
        if len(videos) == 0:
            errors.append(f"{key}: missing exactly one final video in video/ ({', '.join(sorted(VIDEO_EXTENSIONS))})")
        elif len(videos) > 1:
            errors.append(f"{key}: video/ must contain exactly one final video, found {len(videos)}")
        if len(covers) == 0:
            errors.append(f"{key}: missing exactly one final cover in cover/ ({', '.join(sorted(COVER_EXTENSIONS))})")
        elif len(covers) > 1:
            errors.append(f"{key}: cover/ must contain exactly one final cover, found {len(covers)}")
        platform_reports.append(item)

    report = {
        "ok": not errors,
        "packageRoot": str(root),
        "config": str(config_path),
        "notes": str(notes_path),
        "simpleConfig": str(simple_config_path) if simple_config_path.is_file() else None,
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
            video_display = item["video"] or f"{item['videoCount']} candidate(s)"
            cover_display = item["cover"] or f"{item['coverCount']} candidate(s)"
            print(f"  video: {video_display}")
            print(f"  cover: {cover_display}")
        for warning in warnings:
            print(f"Warning: {warning}")
        for error in errors:
            print(f"Error: {error}")

    raise SystemExit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
