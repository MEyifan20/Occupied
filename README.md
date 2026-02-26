# 🛡️ iOS-OmniGuard-Whitelist (Guardian-Standard)

[Adblock Plus 2.0]
! Title: iOS-OmniGuard-Whitelist (Standard Unified Edition)
! Description: 针对 iOS 环境深度优化的全能白名单防误杀护盾。精准放行 Apple 核心服务、国内主流支付/社交链路及关键 CDN，与 Blacklist 完美配合，保障系统 100% 稳定运行。
! Version: 2026.02.26.22
! Codename: Guardian-Standard
! Updated: 2026-02-26 22:10
! -------------------------------------------------------------------------------------------------------

## 📖 项目简介
**iOS-OmniGuard-Whitelist** 是专为 iOS 高级用户打造的“系统级保活”白名单方案。当你在使用高强度的 DNS 黑名单或代理工具去广告时，往往会遭遇 App 无法登录、图片加载失败或系统推送延迟等“误杀”问题。

本库提取了高频误杀节点，通过高优先级的 `@@` 放行规则，为你张开一张隐形护盾。建议将其与 **iOS-OmniGuard-Blacklist** 组合使用，构建完美的攻防闭环。

---

## 🚀 订阅地址

[ jsDelivr CDN 加速 (推荐国内直连) ]
https://cdn.jsdelivr.net/gh/MEyifan20/Whitelist@main/iOS-OmniGuard-Whitelist.txt

[ GitHub 原生地址 ]
https://raw.githubusercontent.com/MEyifan20/Whitelist/main/iOS-OmniGuard-Whitelist.txt

---

## 💎 核心优势
* 🍎 **苹果生态保活**: 强制放行 iCloud 极速同步、App Store 下载、iMessage 及推送服务。
* 💳 **支付链路绿灯**: 确保微信支付、支付宝、银联等金融级 API 节点绝对畅通。
* 🔗 **关键 CDN 修复**: 修复因误杀导致的淘宝/京东图片不显示、B站弹幕断流等次生灾害。
* ⚖️ **底层逻辑闭环**: 采用白名单最高优先级逻辑，免疫一切第三方黑名单库的暴力误杀。

---

## 🛠️ 技术指标 (Technical Metrics)
为了实现极致的系统稳定性，本项目遵循以下放行逻辑：
$$Allow \cap \{Apple\_Core, Finance, Essential\_CDN\} \setminus \{Ad\_Tracker\} = 100\%$$

| 模块名称 | 保护目标 | 策略强度 |
| :--- | :--- | :--- |
| **Apple Core** | iCloud, App Store, 系统的推送与时间同步 | 绝对放行 (Allow) |
| **Finance Shield** | 微信支付、支付宝、银行 App 核心网关 | 绝对放行 (Allow) |
| **CN Essential** | 腾讯/阿里/字节跳动的基础云服务及登录组件 | 修复 (Repair) |
| **Global CDN** | Akamai, Cloudflare 等容易被误杀的云节点 | 保障 (Secure) |

---

## ⚙️ 配置建议
1. **添加路径**：在 AdGuard Pro 等工具中，将上方订阅链接作为**DNS 过滤器**添加（AdGuard 原生支持识别 `@@` 白名单语法）。
2. **优先级设置**：请务必确保该白名单的排序和优先级**高于**所有黑名单，让防护盾在第一层生效。
3. **配合使用**: 强烈建议与本项目的兄弟版本 `iOS-OmniGuard-Blacklist` 组合使用。

---

## 🤖 自动化维护 (Auto-Update)
本项目支持通过 GitHub Actions 实现自动化维护，每日自动更新版本号与时间戳，确保你的规则永远处于激活状态。

---

## 🤝 致谢与声明
* 致谢: 感谢各大开源去广告社区提供的排错反馈。
* 声明: 本项目仅供技术研究与交流使用。

---

## ❤️ 助力项目

- **点亮 Star**：点击右上角 ⭐ Star，这是对我持续维护最大的动力。
- **反馈问题**：请提交 [Issues](https://github.com/MEyifan20/Whitelist/issues)。

---
**iOS-OmniGuard-Whitelist** · 愿你的网络环境干净且自由。

**最后修改时间**：2026-02-26 22:10 (GMT+8)

---
**Maintained by**: [MEyifan20](https://github.com/MEyifan20)  
**License**: [MIT](https://opensource.org/licenses/mit-license.php)
