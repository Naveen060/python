from __future__ import annotations

import json
from pathlib import Path


def pretty_json(path: Path) -> str:
    content = json.loads(path.read_text(encoding="utf-8"))
    return json.dumps(content, indent=2, ensure_ascii=False, sort_keys=True)


def json_summary(path: Path) -> dict:
    content = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(content, dict):
        return {"type": "object", "keys": sorted(content.keys()), "size": len(content)}
    if isinstance(content, list):
        first_type = type(content[0]).__name__ if content else "empty"
        return {"type": "array", "size": len(content), "first_item_type": first_type}
    return {"type": type(content).__name__, "value": content}
