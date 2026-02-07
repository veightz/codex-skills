# codex-skills

Personal Codex skills.

中文说明请见: [README.zh-CN.md](README.zh-CN.md)

## Included skills

- `obsidian-article-import`: import and organize web articles into Obsidian notes with source metadata and local image archiving.

## Prerequisites

### Install uv

macOS (Homebrew):

```bash
brew install uv
```

Linux/macOS (official installer):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify:

```bash
uv --version
```

## Install Skill

Use Codex skill-installer:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo veightz/codex-skills \
  --path skills/obsidian-article-import
```

Then restart Codex to load the new skill.

## Run Skill Script (optional)

The bundled script uses `uv`:

```bash
cd ~/.codex/skills/obsidian-article-import
uv run python scripts/download_images.py --help
```
