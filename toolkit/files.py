from __future__ import annotations

import hashlib
import re
from pathlib import Path


def file_stats(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    words = re.findall(r"\b[\w']+\b", text)
    return {
        "path": str(path),
        "characters": len(text),
        "lines": len(text.splitlines()),
        "words": len(words),
    }


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
