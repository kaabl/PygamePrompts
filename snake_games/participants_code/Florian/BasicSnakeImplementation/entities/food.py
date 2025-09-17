from __future__ import annotations

from typing import Tuple

from .. import utils

GridPos = Tuple[int, int]


class Food:
    def __init__(self, position: GridPos) -> None:
        self.position: GridPos = position

    @classmethod
    def spawn(cls, occupied_positions: list[GridPos]) -> "Food":
        pos = utils.random_empty_cell(occupied_positions)
        return cls(pos)


