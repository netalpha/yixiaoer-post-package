# 蚁小二发布包团队 SOP（按角色版）

## 一句话规则

素材同学只管把过程素材放进 `asset/`，把最终版本放进 `yixiaoer/<platform>/video` 和 `cover`；运营只改 `config.json` 和 `notes.md`；发布执行人用 Codex 检查、dry-run、确认后正式发布。

## 角色总览

| 角色 | 负责什么 | 不负责什么 |
| --- | --- | --- |
| 素材 / 剪辑同学 | 整理素材，导出各平台最终视频和封面 | 不改发布配置，不操作 yxer |
| 运营 / 内容负责人 | 决定发哪些平台、标题、文案、特殊规则 | 不上传、不正式发布 |
| 发布执行人 | 用 Codex 检查、dry-run、确认后发布 | 不从 asset 猜素材，不跳过 dry-run |
| 新电脑配置人 | 安装 skill、配置 yxer 环境 | 不参与内容决策 |
| 管理者 | 验收团队是否按规范交付 | 不需要记命令细节 |

## 素材 / 剪辑同学 SOP

你的目标是交付“各平台最终版本”。

如果项目包已经存在：

1. 直接进入项目包，例如 `post_260701_demo/`。
2. 把原始素材、工程文件、参考资料随便放进 `asset/`。
3. 按平台导出最终视频和封面。
4. 把最终文件放到对应平台目录。

如果项目包还不存在：

1. 从 Dropbox 获取 `yixiaoer-post-package-template.zip`。
2. 解压后得到 `post_package_template/`。
3. 把文件夹改名成实际内容名，例如 `post_260701_demo/`。
4. 后续同样把过程素材放到 `asset/`，把最终版本放到 `yixiaoer/<platform>/`。

最终文件位置：

```text
yixiaoer/douyin/video/main.mp4
yixiaoer/douyin/cover/main.jpg

yixiaoer/kuaishou/video/main.mp4
yixiaoer/kuaishou/cover/main.jpg

yixiaoer/xiaohongshu/video/main.mp4
yixiaoer/xiaohongshu/cover/main.jpg
```

交付标准：

- 启用的平台都有最终视频。
- 启用的平台都有最终封面。
- 文件命名使用 `main.mp4` / `main.jpg`，或确认是支持的替代格式。
- 不要把“待选版本”放进平台最终目录。

## 运营 / 内容负责人 SOP

你只需要改两个文件：

```text
yixiaoer/config.json
yixiaoer/notes.md
```

`config.json` 常改字段：

| 字段 | 怎么填 | 说明 |
| --- | --- | --- |
| `enabledPlatforms` | `["douyin"]` 或 `["douyin","xiaohongshu"]` | 只发布这里列出的平台 |
| `common.title` | 填写通用标题 | 平台未覆盖时使用 |
| `common.description` | 填写通用文案 | 平台未覆盖时使用 |
| `platforms.douyin.title` | 可填抖音专用标题 | 填了就覆盖 common |
| `execution.defaultPublishChannel` | `cloud` 或 `local` | 默认建议 cloud；需要走客户端再用 local |

`notes.md` 写人话规则，结构建议：

```md
## common

- 文案不要改。
- 本次只 dry-run，不正式发布。

## douyin

- 抖音标题控制在 20 字以内。

## xiaohongshu

- 小红书文案可以更种草一点。
```

交接给发布执行人的话术：

```text
发布包路径：/Users/xxx/Desktop/post_260701_demo
本次平台：douyin, xiaohongshu
要求：先 dry-run，确认后再正式发
```

## 发布执行人 SOP

### 为什么有“检查发布包”和“dry-run”两个提示词？

| 动作 | 做什么 | 不会做什么 | 适合什么时候用 |
| --- | --- | --- | --- |
| 检查发布包 | 检查目录、配置、启用平台、视频和封面是否存在 | 不上传素材，不调用平台发布接口 | 素材同学交付后、正式进入发布前 |
| dry-run | 账号检查、prepare、schema、上传、生成 payload、validate、publish --dry-run | 不会正式发布 | 发布前最后确认请求是否可行 |

标准执行顺序：

```text
检查发布包 -> 修缺失文件/配置 -> dry-run -> 负责人确认 -> 正式发布
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

给剪辑同学准备 Dropbox 空模板：

```text
使用仓库里的 release/yixiaoer-post-package-template.zip，上传到 Dropbox 供团队复制解压。
```

## 管理者验收清单

- 团队成员知道 `asset/` 是自由素材区，不参与自动发布。
- 团队成员知道最终发布文件必须放在 `yixiaoer/<platform>/video` 和 `cover`。
- 运营只改 `config.json` 和 `notes.md`。
- 发布执行人理解“检查发布包”和“dry-run”的区别。
- 正式发布前必须有人确认 dry-run 结果。

## Codex 自动化流程

```text
负责人给出发布包路径
-> 检查目录和 config.json
-> 如果最终素材不齐，返回缺失清单
-> 如果素材齐全，执行 dry-run
-> 如果 dry-run 不通过，返回错误原因和修复建议
-> 如果 dry-run 通过，等待负责人确认
-> 正式发布
-> 写入 publish-log.md
```
