import argparse
import hashlib
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

    file_stats_parser = subparsers.add_parser("file-stats", help="Generate quick stats for a text file.")
    file_stats_parser.add_argument("path", type=Path)

    hash_parser = subparsers.add_parser("sha256", help="Generate a SHA-256 hash for a file.")
    hash_parser.add_argument("path", type=Path)

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
    elif args.command == "file-stats":
        print(json.dumps(file_stats(args.path), indent=2))
    elif args.command == "sha256":
        print(sha256_file(args.path))


if __name__ == "__main__":
    main()
