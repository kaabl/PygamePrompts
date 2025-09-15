from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from typing import List


HIGHSCORES_FILE = os.path.join(os.path.dirname(__file__), "highscores.json")
MAX_ENTRIES = 10


@dataclass
class ScoreEntry:
    name: str
    score: int
    speed: int


def load_highscores() -> List[ScoreEntry]:
    if not os.path.exists(HIGHSCORES_FILE):
        return []
    try:
        with open(HIGHSCORES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        result: List[ScoreEntry] = []
        for item in data:
            if (
                isinstance(item, dict)
                and isinstance(item.get("name"), str)
                and isinstance(item.get("score"), int)
                and isinstance(item.get("speed"), int)
            ):
                result.append(ScoreEntry(item["name"], item["score"], item["speed"]))
        return result
    except Exception:
        return []


def save_highscores(entries: List[ScoreEntry]) -> None:
    entries_sorted = sorted(entries, key=lambda e: e.score, reverse=True)[:MAX_ENTRIES]
    with open(HIGHSCORES_FILE, "w", encoding="utf-8") as f:
        json.dump([asdict(e) for e in entries_sorted], f, ensure_ascii=False, indent=2)


def add_score(name: str, score: int, speed: int) -> List[ScoreEntry]:
    entries = load_highscores()
    entries.append(ScoreEntry(name=name, score=score, speed=speed))
    save_highscores(entries)
    return load_highscores()


