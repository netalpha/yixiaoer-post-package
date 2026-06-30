# yixiaoer-post-package

Codex skill for a team-friendly Yixiaoer video publishing package workflow.

This skill helps teams create, inspect, and publish standardized package folders through the existing `yixiaoer` skill and `yxer` CLI.

## Install

```bash
npx skills add "https://github.com/netalpha/yixiaoer-post-package/tree/main/yixiaoer-post-package" -g -y
```

Also install and configure the base `yixiaoer` skill and `yxer` CLI.

```bash
yxer config set-api-key <apiKey>
yxer config set-local-client-id <clientId>
yxer doctor
```

## Package Structure

```text
post_xxxxxx/
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

`asset/` is free-form. Final publish files must be copied into `yixiaoer/<platform>/video/` and `yixiaoer/<platform>/cover/`.

Team members can fill `yixiaoer/简易发布配置.md`. If that file is absent, the workflow uses `yixiaoer/config.json` directly.

For each enabled platform, keep exactly one final video and one final cover. File names do not matter.

## Dropbox Template Zip

For editors who start work before Codex creates a package, use the empty template zip:

```text
release/yixiaoer-post-package-template.zip
```

Workflow:

1. Download or copy the zip into Dropbox.
2. Unzip it.
3. Rename `post_package_template/` to the real content folder, such as `post_260701_demo/`.
4. Put working materials anywhere under `asset/`.
5. Put final platform exports under `yixiaoer/<platform>/video/` and `yixiaoer/<platform>/cover/`.
6. Fill `yixiaoer/简易发布配置.md`, or remove it and maintain `yixiaoer/config.json` directly.

## Common Prompts

```text
Use $yixiaoer-post-package to create a new package at /Users/me/Desktop/post_260701_demo
```

```text
Use $yixiaoer-post-package to inspect /Users/me/Desktop/post_260701_demo
```

Inspection only checks folder structure, enabled platforms, final videos, and final covers. It does not upload files or call publish APIs.

```text
Use $yixiaoer-post-package to dry-run /Users/me/Desktop/post_260701_demo
```

Dry-run enters the real `yixiaoer` / `yxer` pre-publish workflow: account checks, prepare, schema fields, upload, payload generation, validate, and `publish --dry-run`. It does not formally publish.

```text
Use $yixiaoer-post-package to publish /Users/me/Desktop/post_260701_demo
```

The skill validates package structure first, then delegates the actual publish workflow to `yixiaoer` / `yxer`.
