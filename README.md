# Python Utility Toolkit

This repository is now a small but usable Python command-line toolkit instead of a placeholder file. It focuses on lightweight text and JSON helpers that are useful in day-to-day scripting.

## Features

- `slugify` for URL-friendly text conversion
- `stats` for quick text metrics
- `json-pretty` for formatted JSON output
- `file-stats` for file-level text metrics
- `sha256` for checksums

## Run

```powershell
python main.py slugify "Hello World from Python"
python main.py stats "Python is simple and powerful"
python main.py json-pretty sample.json
python main.py file-stats README.md
python main.py sha256 sample.json
```

## Commands

### Slugify

```powershell
python main.py slugify "My Portfolio Project"
```

### Text Stats

```powershell
python main.py stats "This repository is now more useful"
```

### Pretty JSON

```powershell
python main.py json-pretty data.json
```

### File Stats

```powershell
python main.py file-stats README.md
```

### SHA-256

```powershell
python main.py sha256 data.json
```

## Notes

- This project is intentionally dependency-light.
- It works well as a starter repo for Python scripting, automation, or CLI experiments.
