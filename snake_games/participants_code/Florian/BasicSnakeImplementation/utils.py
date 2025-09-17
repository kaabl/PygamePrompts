from __future__ import annotations

import random
from typing import Iterable, Set, Tuple

from . import config

GridPos = Tuple[int, int]


def wrap_position(x: int, y: int) -> GridPos:
    """Wrap (x, y) around the grid bounds if enabled, else clamp inside bounds."""
    if config.WRAP_AROUND:
        return x % config.GRID_COLS, y % config.GRID_ROWS
    return max(0, min(config.GRID_COLS - 1, x)), max(0, min(config.GRID_ROWS - 1, y))


def grid_to_pixel(x: int, y: int) -> Tuple[int, int, int, int]:
    """Return a pygame-friendly rect tuple (left, top, width, height)."""
    return x * config.CELL_SIZE, y * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE


def random_empty_cell(occupied: Iterable[GridPos]) -> GridPos:
    """Return a random grid cell not in occupied; raises if grid is full."""
    occupied_set: Set[GridPos] = set(occupied)
    total_cells = config.GRID_COLS * config.GRID_ROWS
    if len(occupied_set) >= total_cells:
        raise RuntimeError("No empty cells available")

    # Sample uniformly from remaining cells
    while True:
        x = random.randrange(config.GRID_COLS)
        y = random.randrange(config.GRID_ROWS)
        if (x, y) not in occupied_set:
            return x, y


