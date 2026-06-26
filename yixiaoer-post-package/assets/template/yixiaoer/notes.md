# 发布说明

这个文件写人话规则。结构和 `config.json` 对齐：先写 `common`，再写具体平台覆盖规则。

## common

适用于所有平台。

- 手动配置优先修改 `config.json`。
- 只发布 `config.json` 里 `enabledPlatforms` 指定的平台。
- 不根据平台文件夹是否有素材自动发布。
- 不从 `asset/` 直接取素材发布，只从各平台目录读取最终版本。
- 不跳过 `validate`。
- 不跳过 `publish --dry-run`。
- 未确认前不正式发布。

## douyin

覆盖抖音规则。没有特殊要求时保持为空。

- 

## kuaishou

覆盖快手规则。没有特殊要求时保持为空。

- 

## xiaohongshu

覆盖小红书规则。没有特殊要求时保持为空。

- 
