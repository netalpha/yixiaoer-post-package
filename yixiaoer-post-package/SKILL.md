---
name: yixiaoer-post-package
description: "Create, inspect, and publish team Yixiaoer post package folders. Use when the user mentions a yixiaoer post package, post_xxx folder, yixiaoer/config.json, asset/ folder, platform final video/cover folders, or asks to prepare/publish a package to Douyin, Kuaishou, or Xiaohongshu through the existing yixiaoer/yxer workflow."
---

# Yixiaoer Post Package

This skill manages a team folder convention for publishing short videos through the existing `yixiaoer` skill and `yxer` CLI.

It does not replace `yixiaoer`. For any actual account lookup, upload, payload generation, validation, dry-run, or publish operation, load and follow the installed `yixiaoer` skill.

## Folder Contract

A package root contains:

```text
asset/
yixiaoer/
  config.json
  notes.md
  douyin/video/main.mp4
  douyin/cover/main.jpg
  kuaishou/video/main.mp4
  kuaishou/cover/main.jpg
  xiaohongshu/video/main.mp4
  xiaohongshu/cover/main.jpg
```

`asset/` is a free-form workspace. Never infer publish inputs from `asset/` unless the user explicitly says which files to use.

`yixiaoer/config.json` is the single structured config file. `enabledPlatforms` is the only source of truth for which platforms to publish.

`yixiaoer/notes.md` is the single human-readable override file. It has `common` plus platform-specific sections.

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

Then tell the user to put final assets in `yixiaoer/<platform>/video/` and `yixiaoer/<platform>/cover/`, and edit `yixiaoer/config.json`.

### Inspect a Package

When the user gives a package path, run:

```bash
python3 <skill_dir>/scripts/inspect_package.py <package_root>
```

Use the report to identify missing config, invalid platform keys, missing videos, or missing covers.

### Publish a Package

Publishing is a two-skill workflow:

1. Run `inspect_package.py`.
2. If required files are missing, stop and report exactly what to fix.
3. Read `yixiaoer/config.json` and `yixiaoer/notes.md`.
4. For each platform in `enabledPlatforms`, load the installed `yixiaoer` skill and follow its publish-video workflow.
5. Use only that platform's final files:
   - `yixiaoer/<platform>/video/main.mp4` or `main.mov`
   - `yixiaoer/<platform>/cover/main.jpg`, `main.png`, or `main.webp`
6. Generate platform execution artifacts inside the platform folder:
   - `payload.json`
   - `publish-log.md`
7. Always run `yxer validate` and `yxer publish --dry-run` before formal publish.
8. If `requireConfirmBeforePublish` is true, ask for confirmation before formal publish.

## Precedence

```text
latest chat instruction
> yixiaoer/notes.md
> yixiaoer/config.json
> yixiaoer skill and yxer platform rules
```

Platform hard rules always win over package notes or config.

## References

- Package format and team SOP: `references/team-manual.md`
