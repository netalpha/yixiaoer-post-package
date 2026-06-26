# 蚁小二多平台发布包团队手册

## 目标

让团队用统一文件夹准备素材，最终由 Codex 按 `yixiaoer` / `yxer` 流程发布到抖音、快手、小红书。

## 什么时候使用

- 要把一条视频发布到抖音、快手、小红书中的一个或多个平台。
- 团队成员需要先整理素材，再交给负责人或 Codex 发布。
- 同一条素材需要按平台准备不同版本。

## 文件夹结构

```text
post_xxxxxx/
  asset/
  yixiaoer/
    config.json
    notes.md
    douyin/
      video/main.mp4
      cover/main.jpg
    kuaishou/
      video/main.mp4
      cover/main.jpg
    xiaohongshu/
      video/main.mp4
      cover/main.jpg
```

## 角色分工

剪辑或素材同学：

1. 把原始素材、工程文件、参考文件随意放到 `asset/`。
2. 按平台导出最终视频和封面。
3. 把最终版本放进 `yixiaoer/<platform>/video/` 和 `yixiaoer/<platform>/cover/`。

运营或负责人：

1. 修改 `yixiaoer/config.json`。
2. 如有特殊要求，写进 `yixiaoer/notes.md`。
3. 把发布包路径发给 Codex。

Codex：

1. 检查发布包结构。
2. 根据 `enabledPlatforms` 决定发布平台。
3. 调用 `yixiaoer` skill 和 `yxer` CLI 完成账号检查、上传、校验、dry-run、确认和正式发布。
4. 在平台目录记录 `payload.json` 和 `publish-log.md`。

## config.json 怎么改

只改一个文件：

```text
yixiaoer/config.json
```

常改字段：

- `enabledPlatforms`：本次要发布的平台 key。
- `common.title`：通用标题。
- `common.description`：通用文案。
- `platforms.<key>.title`：某个平台专用标题。
- `platforms.<key>.description`：某个平台专用文案。
- `platforms.<key>.account`：指定平台账号。
- `execution.defaultPublishChannel`：默认 `cloud`，需要本机发布时可改为 `local`。

平台 key：

- `douyin`：抖音
- `kuaishou`：快手
- `xiaohongshu`：小红书

## notes.md 怎么写

`notes.md` 是人话补充规则。优先级高于 `config.json`，但不能覆盖平台硬规则。

推荐结构：

```md
## common

- 文案不要改。
- 只 dry-run，不正式发布。

## douyin

- 抖音标题控制在 20 字以内。

## xiaohongshu

- 小红书文案可以更种草一点。
```

## 常用提示词

创建新发布包：

```text
用 yixiaoer-post-package 创建一个新发布包，路径是 /Users/xxx/Desktop/post_260701_demo
```

检查发布包：

```text
检查这个蚁小二发布包：/Users/xxx/Desktop/post_260701_demo
```

发布前 dry-run：

```text
按 yixiaoer 发布包流程检查并 dry-run：/Users/xxx/Desktop/post_260701_demo
```

正式发布：

```text
按 yixiaoer 发布包流程发布：/Users/xxx/Desktop/post_260701_demo
```

只发布某个平台：

```text
把 enabledPlatforms 改成只发 douyin，然后检查发布包。
```

解释失败原因：

```text
根据 publish-log.md 和 yxer 报错，解释这个发布包为什么失败。
```

## 发布前检查清单

- `enabledPlatforms` 只包含本次要发的平台。
- 每个启用平台都有 `video/main.mp4` 或 `video/main.mov`。
- 每个启用平台都有 `cover/main.jpg`、`main.png` 或 `main.webp`。
- 标题和文案已填好。
- 是否正式发布已确认。
- 需要本机发布时，蚁小二客户端已登录在线。
