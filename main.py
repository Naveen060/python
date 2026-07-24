import argparse
import json
from pathlib import Path

from toolkit.files import file_stats, sha256_file
from toolkit.json_tools import json_summary, pretty_json
from toolkit.text import slugify, text_stats


def build_parser():
    parser = argparse.ArgumentParser(
        description="A small Python productivity toolkit for common text, JSON, and file tasks."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    slug_parser = subparsers.add_parser("slugify", help="Convert a string into a URL-friendly slug.")
    slug_parser.add_argument("text")

    stats_parser = subparsers.add_parser("stats", help="Generate quick text statistics.")
    stats_parser.add_argument("text")

    json_parser = subparsers.add_parser("json-pretty", help="Pretty-print a JSON file.")
    json_parser.add_argument("path", type=Path)

    json_summary_parser = subparsers.add_parser("json-summary", help="Summarize the top-level shape of a JSON file.")
    json_summary_parser.add_argument("path", type=Path)

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
    elif args.command == "json-summary":
        print(json.dumps(json_summary(args.path), indent=2))
    elif args.command == "file-stats":
        print(json.dumps(file_stats(args.path), indent=2))
    elif args.command == "sha256":
        print(sha256_file(args.path))


if __name__ == "__main__":
    main()
