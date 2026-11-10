# Zalando 抓取工具

[![Bright Data](https://img.shields.io/badge/Powered%20by-Bright%20Data-FF9A00?style=flat-square)](https://www.bright.cn/) [![爬虫工具 API](https://img.shields.io/badge/Scraper%20API-Available-FF9A00?style=flat-square)](https://www.bright.cn/products/web-scraper/zalando) [![数据集](https://img.shields.io/badge/Dataset-Available-0066CC?style=flat-square)](https://www.bright.cn/products/datasets/zalando) [![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org) [![许可证：MIT](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE)

[![优惠活动](https://github.com/bright-cn/Awesome-Web-Scraping/raw/main/Proxies%20and%20scrapers%20GitHub%20bonus%20banner%20CN.png)](https://www.bright.cn/products/web-scraper/zalando)

> **由 [Bright Data](https://www.bright.cn/) 提供支持的 Zalando 数据。**

此代码库提供两种大规模访问 Zalando 数据的方法：

- **[方法 1：Bright Data Zalando 爬虫工具 API](#方法-1bright-data-zalando-爬虫工具-api)**（推荐），完全托管的企业级爬虫 API，可自动处理代理、CAPTCHA 和扩展。
- **[方法 2：Bright Data Zalando 数据集](#方法-2bright-data-zalando-数据集)**，可随时下载的预采集 Zalando 数据集，无需抓取。

## 目录

- [为什么使用 Bright Data 抓取 Zalando？](#为什么使用-bright-data-抓取-zalando)
- [方法 1：Bright Data Zalando 爬虫工具 API](#方法-1bright-data-zalando-爬虫工具-api)
  - [入门指南](#zalando-爬虫工具-api-入门指南)
  - [1. Zalando 数据](#1-zalando-数据)
- [方法 2：Bright Data Zalando 数据集](#方法-2bright-data-zalando-数据集)
- [数据采集方式](#数据采集方式)

## 为什么使用 Bright Data 抓取 Zalando？

抓取 Zalando 面临多项挑战：

- 速率限制：Zalando 会监控请求频率，并可能封禁超过限制的 IP。
- CAPTCHA 检测：自动访问可能会触发 CAPTCHA 验证。
- 身份验证障碍：部分数据需要登录才能访问，并且平台会检测自动化操作。
- 动态内容加载：仅使用简单的 HTTP 请求难以抓取由 JavaScript 渲染的内容。
- IP 封禁：从同一 IP 重复发送请求可能会导致封禁。

Bright Data 的 Zalando 爬虫工具 API 可通过以下功能解决这些问题：

- ✅ **内置动态代理**：自动绕过基于 IP 的速率限制
- ✅ **验证码破解**：无需任何额外设置即可处理机器人检测
- ✅ **结构化数据输出**：获取可直接用于分析的整洁 JSON
- ✅ **无需基础设施**：支持任意规模的云端托管抓取
- ✅ **99.9% 可用性 SLA**：为业务关键型工作流提供可靠的数据采集

## 方法 1：Bright Data Zalando 爬虫工具 API

[Bright Data Zalando 爬虫工具 API](https://www.bright.cn/products/web-scraper/zalando) 是一款完全托管的解决方案，无需设置任何基础设施。

### Zalando 爬虫工具 API 入门指南

1. **注册**[免费的 Bright Data 账户](https://www.bright.cn/)
2. **前往** [Zalando 爬虫工具 API](https://www.bright.cn/products/web-scraper/zalando)
3. 从控制面板**获取 API 令牌**
4. **安装** `requests` 库：`pip install requests`
5. **运行** `zalando_scraper_api_codes/` 中的任意脚本

### 1. Zalando 数据

采集 Zalando 商品数据。

#### 输入参数

| 字段 | 类型 | 必填 | 说明 |
|-------|------|----------|-------------|
| `url` | 字符串 | 是 | 要抓取的 Zalando 商品 URL |
| `limit` | 整数 | 否 | 返回结果的最大数量 |
| `include_errors` | 布尔值 | 否 | 在响应中包含错误详情 |
| `notify` | url | 否 | 采集完成时用于接收通知的 Webhook URL |
| `format` | 枚举 | 否 | 输出格式：`JSON`、`NDJSON`、`JSON Lines`、`CSV` |

#### 响应示例

```json
{
  "condition": "NewCondition",
  "country_code": "de",
  "db_source": "1770988297087",
  "domain": "zalando.de",
  "sku": "OP421U047-Q11",
  "url": "https://zalando.de/only-petite-onlsascha-sherpa-jacket-klassischer-mantel-black-op421u047-q11.html"
}
```

👉 查看[完整 Python 代码](zalando_scraper_api_codes/zalando_scraper.py)

## 方法 2：Bright Data Zalando 数据集

如果你需要无需编写任何抓取代码即可使用的数据，[Bright Data Zalando 数据集](https://www.bright.cn/products/datasets/zalando)可提供预先采集并定期更新的数据，支持即时下载。

**为什么使用数据集而不是 API？**

- 📦 **即时访问**：无需设置、无需代码，也无需等待采集
- 🔄 **定期更新**：按固定计划刷新，持续提供最新数据
- 📊 **多种格式**：支持下载为 JSON、JSONL 或 CSV
- 🌍 **海量规模**：涵盖 Zalando 所有主要类别的数百万条记录
- ✅ **完全合规**：数据来源符合道德规范，并已获得合法授权

👉 **[探索 Zalando 数据集](https://www.bright.cn/products/datasets/zalando)**

## 数据采集方式

| 功能 | Bright Data 爬虫工具 API | Bright Data 数据集 |
|---------|------------------------|---------------------|
| 所需设置 | 仅需 API 令牌 | 无 |
| 实时数据 | ✅ 是 | ❌ 预先采集 |
| 自定义查询 | ✅ 完全控制 | ❌ 固定架构 |
| 包含代理 | ✅ 内置动态代理 | N/A |
| 验证码破解 | ✅ 自动 | N/A |
| 规模 | 无限制 | 无限制 |
| 结构化输出 | ✅ JSON / NDJSON / JSON Lines / CSV | ✅ JSON / JSONL / CSV |
| 支持 | 企业级全天候支持 | 企业级全天候支持 |

---

🔗 **了解更多**：[https://www.bright.cn/products/web-scraper/zalando](https://www.bright.cn/products/web-scraper/zalando)
