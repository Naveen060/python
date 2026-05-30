import argparse
import json
import re
from collections import Counter
from pathlib import Path


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", cleaned).strip("-")


def text_stats(text: str) -> dict:
    words = re.findall(r"\b[\w']+\b", text.lower())
    return {
        "characters": len(text),
        "words": len(words),
        "unique_words": len(set(words)),
        "top_words": Counter(words).most_common(5),
    }


def pretty_json(path: Path) -> str:
    content = json.loads(path.read_text(encoding="utf-8"))
    return json.dumps(content, indent=2, ensure_ascii=False, sort_keys=True)


def build_parser():
    parser = argparse.ArgumentParser(
        description="A small Python productivity toolkit for common text and JSON tasks."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    slug_parser = subparsers.add_parser("slugify", help="Convert a string into a URL-friendly slug.")
    slug_parser.add_argument("text")

    stats_parser = subparsers.add_parser("stats", help="Generate quick text statistics.")
    stats_parser.add_argument("text")

    json_parser = subparsers.add_parser("json-pretty", help="Pretty-print a JSON file.")
    json_parser.add_argument("path", type=Path)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "slugify":
        print(slugify(args.text))
    elif args.command == "stats":
        result = text_stats(args.text)
        print(json.dumps(result, indent=2))
    elif args.command == "json-pretty":
        print(pretty_json(args.path))


if __name__ == "__main__":
    main()
