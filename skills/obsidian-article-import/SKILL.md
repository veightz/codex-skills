---
name: obsidian-article-import
description: Import and organize a web article into an Obsidian note. Use when user asks to导入文章/整理链接内容/保存来源，并希望记录原始链接、采集日期、作者来源，且尽量将关键图片下载到本地 attachments 以降低外链依赖。
metadata:
  short-description: Import article to Obsidian with source + local images
---

# Obsidian Article Import

## 何时使用
- 用户提到“导入文章”“整理网页内容到笔记”“保存原文链接”。
- 用户要求“图片尽量本地化”“避免后续外链失效”。

## 输入
- 必需：文章 URL。
- 可选：目标文件名、目标目录、是否全量下载图片（默认仅关键图）。

## 输出要求
- 产出一篇 Obsidian Markdown 笔记，至少包含：
  - 原始链接（URL）
  - 采集日期（绝对日期）
  - 来源与作者（若可获取）
  - 结构化摘要（结论、要点、行动项）
- 图片处理：
  - 优先下载关键图片到 `attachments/`。
  - 正文优先引用本地图片路径。
  - 下载失败的图片要标注“外链保留（待补档）”。

## 执行流程
1. 抓取文章内容与元信息（标题、作者、来源、发布时间、主图/内文图）。
2. 生成笔记标题与文件名（默认：`<主题>-YYYY-MM-DD.md`）。
3. 按仓库模板组织内容；若存在 `templates/文章整理模板.md`，优先沿用该结构。
4. 识别关键图片并下载到 `attachments/`：
   - 命名建议：`<slug>-<YYYY-MM-DD>-<index>.<ext>`。
   - 同名冲突时自动追加序号。
5. 将可下载图片替换为本地路径引用；失败项保留外链并登记。
6. 进行质量检查：
   - 来源信息完整
   - 至少一段摘要结论
   - 行动项可执行
   - 图片归档清单清楚

## 快捷指令示例
- “用 `obsidian-article-import` 整理这篇文章：<URL>，关键图片本地化。”
- “导入这个链接并生成笔记，图片尽量下载到 attachments。”

## 附带脚本
- `scripts/download_images.py`：批量下载图片 URL 到本地目录。
- 默认使用 `uv` 执行，保证不同机器运行环境一致。
- 如果页面图链已提取为列表文件，可直接执行：
  - `uv run python scripts/download_images.py --urls-file /tmp/img_urls.txt --out-dir attachments --prefix article-2026-02-07`
