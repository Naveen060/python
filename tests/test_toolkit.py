import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from toolkit.json_tools import json_summary
from toolkit.text import slugify, text_stats


def test_slugify_handles_spaces_and_symbols():
    assert slugify("My Portfolio Project!") == "my-portfolio-project"


def test_text_stats_counts_sentences():
    stats = text_stats("One sentence. Two sentence?")
    assert stats["sentences"] == 2


def test_json_summary_reports_object_keys(tmp_path: Path):
    sample = tmp_path / "sample.json"
    sample.write_text(json.dumps({"name": "Naveen", "role": "developer"}), encoding="utf-8")
    summary = json_summary(sample)
    assert summary["type"] == "object"
    assert "name" in summary["keys"]
