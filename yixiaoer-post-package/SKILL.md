---
name: yixiaoer-post-package
description: "Create, inspect, and publish team Yixiaoer post package folders. Use when the user mentions a yixiaoer post package, post_xxx folder, yixiaoer/简易发布配置.md, yixiaoer/config.json, asset/ folder, platform final video/cover folders, or asks to prepare/publish a package to Douyin, Kuaishou, or Xiaohongshu through the existing yixiaoer/yxer workflow."
---

# Yixiaoer Post Package

This skill manages a team folder convention for publishing short videos through the existing `yixiaoer` skill and `yxer` CLI.

It does not replace `yixiaoer`. For any actual account lookup, upload, payload generation, validation, dry-run, or publish operation, load and follow the installed `yixiaoer` skill.

## Folder Contract

A package root contains:

```text
asset/
yixiaoer/
  简易发布配置.md
  config.json
  notes.md
  douyin/video/<one final .mp4 or .mov>
  douyin/cover/<one final .jpg/.jpeg/.png/.webp>
  kuaishou/video/<one final .mp4 or .mov>
  kuaishou/cover/<one final .jpg/.jpeg/.png/.webp>
  xiaohongshu/video/<one final .mp4 or .mov>
  xiaohongshu/cover/<one final .jpg/.jpeg/.png/.webp>
```

`asset/` is a free-form workspace. Never infer publish inputs from `asset/` unless the user explicitly says which files to use.

`yixiaoer/简易发布配置.md` is the optional team-facing configuration file. Team members can edit this file instead of JSON.

`yixiaoer/config.json` is the structured machine-facing config. If `简易发布配置.md` exists, sync `config.json` from it before inspection or publishing. If `简易发布配置.md` does not exist, use `config.json` directly.

`yixiaoer/notes.md` is an optional executor notes file for extra guardrails. It should not be used as the primary business configuration.

For each enabled platform, the platform `video/` folder must contain exactly one supported video file and the platform `cover/` folder must contain exactly one supported cover image. File names do not matter.

## Platform Keys

- `douyin` -> `抖音`
- `kuaishou` -> `快手`
- `xiaohongshu` -> `小红书`

## Common Tasks

### Create a Package

When the user asks to create a new package, copy `assets/template/`.

Preferred command:

```bash
python3 <skill_dir>/scripts/create_package.py <destination>
```

Then tell the user to put final assets in `yixiaoer/<platform>/video/` and `yixiaoer/<platform>/cover/`, keep exactly one final file in each folder, and edit `yixiaoer/简易发布配置.md` or `yixiaoer/config.json`.

### Sync Config

Before inspecting or publishing a package, run the sync command. It syncs the machine config from `简易发布配置.md` when that file exists; otherwise it leaves `config.json` untouched and reports that the package will use `config.json` directly.

```bash
python3 <skill_dir>/scripts/sync_config_from_spec.py <package_root>
```

If `简易发布配置.md` exists but is ambiguous, stop and ask the team to fix it. If `简易发布配置.md` is missing, continue with `config.json`.

### Inspect a Package

When the user gives a package path, run:

```bash
python3 <skill_dir>/scripts/sync_config_from_spec.py <package_root>
python3 <skill_dir>/scripts/inspect_package.py <package_root>
```

Use the report to identify missing config, invalid platform keys, missing videos, missing covers, or platform folders containing more than one supported final video/cover.

### Publish a Package

Publishing is a two-skill workflow:

1. Run `sync_config_from_spec.py`; it uses `yixiaoer/简易发布配置.md` if present, otherwise `yixiaoer/config.json`.
2. Run `inspect_package.py`.
3. If required files are missing, stop and report exactly what to fix.
4. Read `yixiaoer/config.json` and `yixiaoer/notes.md`.
5. For each platform in `enabledPlatforms`, load the installed `yixiaoer` skill and follow its publish-video workflow.
6. Use only that platform's unique final files from `inspect_package.py`:
   - exactly one supported video in `yixiaoer/<platform>/video/`
   - exactly one supported cover in `yixiaoer/<platform>/cover/`
7. Generate platform execution artifacts inside the platform folder:
   - `payload.json`
   - `publish-log.md`
8. Always run `yxer validate` and `yxer publish --dry-run` before formal publish.
9. If `requireConfirmBeforePublish` is true, ask for confirmation before formal publish.

## Precedence

```text
latest chat instruction
> yixiaoer/简易发布配置.md, when present
> yixiaoer/config.json
> yixiaoer/notes.md
> yixiaoer skill and yxer platform rules
```

Platform hard rules always win over package notes or config.

## References

- Package format and team SOP: `references/team-manual.md`
