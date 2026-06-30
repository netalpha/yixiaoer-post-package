# 蚁小二发布包团队 SOP（按角色版）

## 一句话规则

素材同学只管把过程素材放进 `asset/`，把每个平台的最终版本放进对应 `video/` 和 `cover/` 文件夹；运营优先填写 `yixiaoer/简易发布配置.md`；如果没有这个文件，就维护 `config.json`；发布执行人用 Codex 同步配置、检查、dry-run、确认后正式发布。

## 角色总览

| 角色 | 负责什么 | 不负责什么 |
| --- | --- | --- |
| 素材 / 剪辑同学 | 整理素材，导出各平台最终视频和封面 | 不改发布配置，不操作 yxer |
| 运营 / 内容负责人 | 填写发布平台、账号、标题、文案、发布时间等业务信息 | 不改 `config.json`，不上传、不正式发布 |
| 发布执行人 | 用 Codex 同步配置、检查、dry-run、确认后发布 | 不从 `asset/` 猜素材，不跳过 dry-run |
| 新电脑配置人 | 安装 skill、配置 yxer 环境 | 不参与内容决策 |
| 管理者 | 验收团队是否按规范交付 | 不需要记命令细节 |

## 素材 / 剪辑同学 SOP

你的目标是交付“各平台最终版本”。

1. 拿到项目包，例如 `post_260701_demo/`。
2. 把原始素材、工程文件、参考资料随便放进 `asset/`。
3. 按平台导出最终视频和封面。
4. 把最终文件放到对应平台目录。

最终文件位置：

```text
yixiaoer/douyin/video/
yixiaoer/douyin/cover/

yixiaoer/kuaishou/video/
yixiaoer/kuaishou/cover/

yixiaoer/xiaohongshu/video/
yixiaoer/xiaohongshu/cover/
```

交付标准：

- 启用的平台都有最终视频。
- 启用的平台都有最终封面。
- 每个启用平台的 `video/` 里只放 1 个最终视频。
- 每个启用平台的 `cover/` 里只放 1 张最终封面。
- 文件名无所谓，不强制 `main.mp4` 或 `main.png`。
- 不要把“待选版本”放进平台最终目录。

## 运营 / 内容负责人 SOP

你只需要填写一个文件：

```text
yixiaoer/简易发布配置.md
```

推荐格式：

```md
- 发布平台：抖音
- 发布账户：RP温暖之家-南
- 标题：视网膜色素变性的核心错位真相
- 描述：#视网膜色素变性  #RP眼病  #眼健康科普
- 发布时间：立即发布
- 是否挂预约卡：否
- 是否挂小黄车：否
```

填写规则：

- `发布平台` 可填 `抖音`、`快手`、`小红书`；多平台用逗号分隔。
- `发布时间` 填 `立即发布` 表示不定时发布。
- 需要预约时可填类似 `2026年7月01日19：31`。
- 如果存在 `简易发布配置.md`，不要直接修改 `config.json`，它由 Codex 从简易配置同步生成。
- 如果没有 `简易发布配置.md`，就直接维护 `config.json`。

交接给发布执行人的话术：

```text
发布包路径：/Users/xxx/Desktop/post_260701_demo
简易发布配置.md 已填写，素材已放入对应平台目录。
要求：先 dry-run，确认后再正式发。
```

## 发布执行人 SOP

### 为什么有“同步配置”“检查发布包”和“dry-run”？

| 动作 | 做什么 | 不会做什么 | 适合什么时候用 |
| --- | --- | --- | --- |
| 同步配置 | 存在 `简易发布配置.md` 时从它生成 `config.json`；不存在时直接使用 `config.json` | 不上传素材，不发布 | 进入检查和发布前 |
| 检查发布包 | 检查目录、启用平台、唯一视频和唯一封面 | 不上传素材，不调用平台发布接口 | 素材同学交付后、正式进入发布前 |
| dry-run | 账号检查、prepare、schema、上传、生成 payload、validate、publish --dry-run | 不会正式发布 | 发布前最后确认请求是否可行 |

标准执行顺序：

```text
同步配置 -> 检查发布包 -> 修缺失文件/配置 -> dry-run -> 负责人确认 -> 正式发布 -> 写入日志
```

常用提示词：

```text
检查这个蚁小二发布包：/Users/xxx/Desktop/post_260701_demo
```

```text
按 yixiaoer 发布包流程检查并 dry-run：/Users/xxx/Desktop/post_260701_demo
```

```text
按 yixiaoer 发布包流程发布：/Users/xxx/Desktop/post_260701_demo
```

```text
根据 publish-log.md 和 yxer 报错，解释这个发布包为什么失败。
```

## 新电脑配置人 SOP

安装发布包 skill：

```bash
npx skills add "https://github.com/netalpha/yixiaoer-post-package/tree/main/yixiaoer-post-package" -g -y
```

配置 `yxer`：

```bash
yxer config set-api-key <apiKey>
yxer config set-local-client-id <clientId>
yxer doctor
```

创建新发布包：

```text
用 yixiaoer-post-package 创建一个新发布包，路径是 /Users/xxx/Desktop/post_260701_demo
```

## 管理者验收清单

- 团队成员知道 `asset/` 是自由素材区，不参与自动发布。
- 团队成员知道最终发布文件必须放在 `yixiaoer/<platform>/video` 和 `cover`。
- 团队成员知道每个启用平台只保留 1 个最终视频和 1 张最终封面。
- 运营优先填写 `简易发布配置.md`；没有该文件时维护 `config.json`。
- 发布执行人理解“同步配置”“检查发布包”和“dry-run”的区别。
- 正式发布前必须有人确认 dry-run 结果。

## Codex 自动化流程

```text
负责人给出发布包路径
-> 若存在简易发布配置.md，读取并同步生成 config.json
-> 若不存在简易发布配置.md，直接读取 config.json
-> 检查启用平台目录和唯一素材
-> 如果最终素材不齐或数量不唯一，返回缺失/重复清单
-> 如果素材齐全，执行 dry-run
-> 如果 dry-run 不通过，返回错误原因和修复建议
-> 如果 dry-run 通过，等待负责人确认
-> 正式发布
-> 写入 publish-log.md
```
