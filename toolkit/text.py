from __future__ import annotations

import re
from collections import Counter


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", cleaned).strip("-")


def text_stats(text: str) -> dict:
    words = re.findall(r"\b[\w']+\b", text.lower())
    sentences = [part for part in re.split(r"[.!?]+", text) if part.strip()]
    return {
        "characters": len(text),
        "words": len(words),
        "unique_words": len(set(words)),
        "sentences": len(sentences),
        "top_words": Counter(words).most_common(5),
    }
