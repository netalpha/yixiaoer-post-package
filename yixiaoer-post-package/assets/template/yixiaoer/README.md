# yixiaoer 最终发布区

这里是发布执行区。发布时默认只读取本目录中的配置和定稿素材。

## 唯一配置文件

所有需要你手动修改的结构化配置都集中在：

```text
config.json
```

具体发布哪些平台，只看 `config.json` 里的 `enabledPlatforms`。

不要根据平台文件夹是否存在、是否有素材来自动发布，避免误发旧素材。

人话说明统一写在：

```text
notes.md
```

`notes.md` 也按 common + 平台覆盖的方式写，不在各平台目录里分散维护。

## 优先级

```text
聊天最新指令
> yixiaoer/notes.md
> yixiaoer/config.json
> yixiaoer skill / yxer 平台硬规则
```

## 发布来源

每个平台的最终发布素材固定放在：

```text
yixiaoer/<platform>/video/main.mp4
yixiaoer/<platform>/cover/main.jpg
```

请把最终版本放进对应平台目录。发布时我只认这里的文件，不从 `asset/` 自动挑选。

## 执行产物

发布时我可以在对应平台目录生成：

```text
yixiaoer/<platform>/payload.json
yixiaoer/<platform>/publish-log.md
```
