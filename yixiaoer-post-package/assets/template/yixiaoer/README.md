# yixiaoer 最终发布区

这里是发布执行区。发布时默认只读取本目录中的简易配置、机器配置和定稿素材。

## 团队填写入口

团队成员只需要填写：

```text
简易发布配置.md
```

如果 `简易发布配置.md` 存在，Codex 会先从它同步生成 `config.json`。

如果 `简易发布配置.md` 不存在，就直接以 `config.json` 为准。

## 发布平台

具体发布哪些平台，以同步后的 `config.json` 里的 `enabledPlatforms` 为准。

不要根据平台文件夹是否存在、是否有素材来自动发布，避免误发旧素材。

## 优先级

```text
聊天最新指令
> yixiaoer/简易发布配置.md（存在时）
> yixiaoer/config.json
> yixiaoer/notes.md
> yixiaoer skill / yxer 平台硬规则
```

## 发布来源

每个平台的最终发布素材放在：

```text
yixiaoer/<platform>/video/
yixiaoer/<platform>/cover/
```

每个启用平台要求：

- `video/` 里只放 1 个最终视频。
- `cover/` 里只放 1 张最终封面。
- 文件名无所谓，不强制 `main.mp4` 或 `main.png`。
- 不从 `asset/` 自动挑选素材。

## 执行产物

发布时我可以在对应平台目录生成：

```text
yixiaoer/<platform>/payload.json
yixiaoer/<platform>/publish-log.md
```
