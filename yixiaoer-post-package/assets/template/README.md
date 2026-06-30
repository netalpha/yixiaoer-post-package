# 多平台视频发布包模板

这个文件夹是一条内容的项目包。复制本目录并改名为本次内容名称，例如：

```text
post_260626/
```

## 使用规则

1. `asset/` 是自由素材区，不规定结构，你可以随便放素材。模板里保持空目录。
2. `yixiaoer/` 是最终发布区，发布时只读取这里的简易配置、机器配置和定稿素材。
3. 团队成员优先填写 `yixiaoer/简易发布配置.md`。
4. 如果没有 `yixiaoer/简易发布配置.md`，就直接以 `yixiaoer/config.json` 为准。
5. 具体发布哪些平台，以 `config.json` 里的 `enabledPlatforms` 为准，不根据文件夹是否有素材自动判断。
6. 每个平台必须先通过 `validate` 和 `publish --dry-run`，确认后才正式发布。

## 推荐流程

1. 把素材随意放入 `asset/`，按你自己的方式整理。
2. 确定最终版本后，把对应平台最终视频和封面放到 `yixiaoer/<platform>/video/` 与 `yixiaoer/<platform>/cover/`。
3. 每个启用平台的 `video/` 只保留 1 个最终视频，`cover/` 只保留 1 张最终封面；文件名无所谓。
4. 填写 `yixiaoer/简易发布配置.md`；如果没有这个文件，则维护 `yixiaoer/config.json`。
5. 把整个项目包路径发给我。

## asset 规则

`asset/` 不参与自动发布，我不会从里面猜要用哪个文件。

如果你临时想让我从 `asset/` 中挑选或复制素材，请在聊天里明确说明。
