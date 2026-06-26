# 多平台视频发布包模板

这个文件夹是一条内容的项目包。复制本目录并改名为本次内容名称，例如：

```text
post_260626/
```

## 使用规则

1. `asset/` 是自由素材区，不规定结构，你可以随便放素材。模板里保持空目录。
2. `yixiaoer/` 是最终发布区，发布时只读取这里的定稿配置和定稿素材。
3. 所有发布配置只改 `yixiaoer/config.json`。
4. 具体发布哪些平台，只看 `yixiaoer/config.json` 里的 `enabledPlatforms`，不要根据文件夹是否有素材自动判断。
5. 每个平台必须先通过 `validate` 和 `publish --dry-run`，确认后才正式发布。

## 推荐流程

1. 把素材随意放入 `asset/`，按你自己的方式整理。
2. 确定最终版本后，把对应平台最终视频和封面放到 `yixiaoer/<platform>/video/` 与 `yixiaoer/<platform>/cover/`。
3. 只修改 `yixiaoer/config.json`。
4. 把整个项目包路径发给我。

## asset 规则

`asset/` 不参与自动发布，我不会从里面猜要用哪个文件。

如果你临时想让我从 `asset/` 中挑选或复制素材，请在聊天里明确说明。
