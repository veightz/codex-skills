# codex-skills

个人 Codex Skills 仓库。

English version: [README.md](README.md)

## 已包含的 Skill

- `obsidian-article-import`：将网页文章导入并整理为 Obsidian 笔记，保留来源元信息并尽量将关键图片本地化归档。

## 前置依赖

### 安装 uv

macOS（Homebrew）：

```bash
brew install uv
```

Linux/macOS（官方安装脚本）：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows（PowerShell）：

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

验证安装：

```bash
uv --version
```

## 安装 Skill

使用 Codex 的 skill-installer：

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo veightz/codex-skills \
  --path skills/obsidian-article-import
```

安装后重启 Codex 以加载新 skill。

## 运行 Skill 脚本（可选）

该 skill 自带脚本默认使用 `uv` 运行：

```bash
cd ~/.codex/skills/obsidian-article-import
uv run python scripts/download_images.py --help
```
