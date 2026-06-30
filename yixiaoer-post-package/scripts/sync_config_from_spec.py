#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


PLATFORM_BY_NAME = {
    "抖音": "douyin",
    "douyin": "douyin",
    "快手": "kuaishou",
    "kuaishou": "kuaishou",
    "小红书": "xiaohongshu",
    "xiaohongshu": "xiaohongshu",
}

PLATFORM_LABELS = {
    "douyin": "抖音",
    "kuaishou": "快手",
    "xiaohongshu": "小红书",
}


def parse_simple_config(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line.startswith("-"):
            continue
        line = line.lstrip("-").strip()
        if "：" in line:
            key, value = line.split("：", 1)
        elif ":" in line:
            key, value = line.split(":", 1)
        else:
            continue
        values[key.strip()] = value.strip()
    return values


def parse_platforms(value: str) -> list[str]:
    parts = [part.strip() for part in re.split(r"[,，、/]+", value) if part.strip()]
    keys = []
    for part in parts:
        key = PLATFORM_BY_NAME.get(part)
        if not key:
            raise ValueError(f"unknown platform in 简易发布配置.md: {part}")
        if key not in keys:
            keys.append(key)
    return keys


def parse_schedule(value: str | None):
    if not value:
        return None
    compact = value.strip()
    if compact in {"立即发布", "马上发布", "即时发布", "立刻发布", "不定时", "无", "否"}:
        return None

    normalized = compact.replace("：", ":")
    match = re.search(r"(\d{4})年\s*(\d{1,2})月\s*(\d{1,2})日\s*(\d{1,2})[:点]\s*(\d{1,2})", normalized)
    if match:
        year, month, day, hour, minute = (int(part) for part in match.groups())
        return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}"

    match = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})\s+(\d{1,2}):(\d{1,2})", normalized)
    if match:
        year, month, day, hour, minute = (int(part) for part in match.groups())
        return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}"

    raise ValueError(f"unsupported 发布时间 format: {value}")


def default_config() -> dict:
    return {
        "_do_not_modify_comment": "机器配置文件：优先由 yixiaoer/简易发布配置.md 同步生成；如果该文件不存在，则直接使用本文件。",
        "_edit_me_comment": "同步来源：发布平台、发布账户、标题、描述、发布时间、是否挂预约卡、是否挂小黄车。平台目录只需保留 1 个视频和 1 张封面，文件名不强制为 main.*。",
        "enabledPlatforms": [],
        "availablePlatforms": PLATFORM_LABELS,
        "execution": {
            "mode": "publish-selected-platforms-only",
            "requireDryRunBeforePublish": True,
            "requireConfirmBeforePublish": True,
            "defaultPublishChannel": "cloud",
        },
        "common": {
            "_edit_me_comment": "这里可由简易发布配置.md 同步。平台配置里的非 null 字段会覆盖这里。",
            "type": "video",
            "title": None,
            "description": None,
            "schedule": None,
            "publishChannel": None,
            "allowDescriptionRewrite": False,
        },
        "platforms": {},
    }


def platform_config(key: str) -> dict:
    options = {
        "location": None,
        "music": None,
        "collection": None,
        "challenge": None,
        "goods": None,
    }
    if key == "xiaohongshu":
        options.pop("music")
        options.pop("challenge")
        options["topics"] = None
    return {
        "platform": PLATFORM_LABELS[key],
        "account": None,
        "title": None,
        "description": None,
        "schedule": None,
        "publishChannel": None,
        "options": options,
    }


def main():
    parser = argparse.ArgumentParser(description="Sync yixiaoer/config.json from yixiaoer/简易发布配置.md when present.")
    parser.add_argument("package_root", help="Package root folder")
    parser.add_argument("--json", action="store_true", help="Print JSON report")
    args = parser.parse_args()

    root = Path(args.package_root).expanduser().resolve()
    yixiaoer_dir = root / "yixiaoer"
    simple_config_path = yixiaoer_dir / "简易发布配置.md"
    config_path = yixiaoer_dir / "config.json"

    if not simple_config_path.is_file():
        if not config_path.is_file():
            raise SystemExit(f"neither yixiaoer/简易发布配置.md nor yixiaoer/config.json exists under: {yixiaoer_dir}")
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
        except Exception as exc:
            raise SystemExit(f"invalid config.json: {exc}") from exc
        enabled = config.get("enabledPlatforms", [])
        report = {
            "ok": True,
            "source": "config.json",
            "packageRoot": str(root),
            "simpleConfig": None,
            "config": str(config_path),
            "enabledPlatforms": enabled,
            "schedule": config.get("common", {}).get("schedule"),
        }
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(f"Using existing config: {config_path}")
            print(f"Enabled: {', '.join(enabled) if isinstance(enabled, list) else enabled}")
        return

    spec = parse_simple_config(simple_config_path)
    enabled = parse_platforms(spec.get("发布平台", ""))
    if not enabled:
        raise SystemExit("简易发布配置.md must include 发布平台")

    config = default_config()
    if config_path.is_file():
        try:
            existing = json.loads(config_path.read_text(encoding="utf-8"))
            config["execution"].update(existing.get("execution", {}))
        except Exception:
            pass

    config["enabledPlatforms"] = enabled
    config["common"]["title"] = spec.get("标题")
    config["common"]["description"] = spec.get("描述")
    config["common"]["schedule"] = parse_schedule(spec.get("发布时间"))
    config["platforms"] = {key: platform_config(key) for key in PLATFORM_LABELS}

    account = spec.get("发布账户")
    for key in enabled:
        if len(enabled) == 1 and account:
            config["platforms"][key]["account"] = account

    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = {
        "ok": True,
        "source": "简易发布配置.md",
        "packageRoot": str(root),
        "simpleConfig": str(simple_config_path),
        "config": str(config_path),
        "enabledPlatforms": enabled,
        "schedule": config["common"]["schedule"],
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Synced config: {config_path}")
        print(f"Enabled: {', '.join(enabled)}")
        print(f"Schedule: {config['common']['schedule'] or 'immediate'}")


if __name__ == "__main__":
    main()
