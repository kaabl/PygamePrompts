from __future__ import annotations

from collections import deque
from typing import Deque, Iterable, List, Tuple

from .. import config
from .. import utils

GridPos = Tuple[int, int]
Direction = Tuple[int, int]


class Snake:
    def __init__(self, start: GridPos, length: int = 3, direction: Direction = (1, 0)) -> None:
        self.direction: Direction = direction
        self.pending_growth: int = 0
        # Head at index 0
        self.body: Deque[GridPos] = deque()
        x, y = start
        # Initialize horizontally with head at (x, y) and body trailing to the left
        for i in range(length):
            self.body.append((x - i, y))

        # Normalize inside bounds
        self.body = deque((utils.wrap_position(x, y) for (x, y) in self.body))

    def head(self) -> GridPos:
        return self.body[0]

    def occupies(self) -> List[GridPos]:
        return list(self.body)

    def set_direction(self, direction: Direction) -> None:
        self.direction = direction

    def move(self) -> None:
        hx, hy = self.head()
        dx, dy = self.direction
        nx, ny = utils.wrap_position(hx + dx, hy + dy)

        self.body.appendleft((nx, ny))
        if self.pending_growth > 0:
            self.pending_growth -= 1
        else:
            self.body.pop()

    def grow(self, amount: int = 1) -> None:
        self.pending_growth += amount

    def is_self_collision(self) -> bool:
        head = self.head()
        # If head appears more than once in the body
        return head in list(self.body)[1:]


