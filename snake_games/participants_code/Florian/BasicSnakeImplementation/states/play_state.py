from __future__ import annotations

from typing import Optional

import pygame

from .. import config
from .. import ui
from .. import input as input_mod
from ..entities.snake import Snake
from ..entities.food import Food


class PlayState:
    def __init__(self) -> None:
        # Start snake in center, moving right, length 3
        center = (config.GRID_COLS // 2, config.GRID_ROWS // 2)
        self.snake = Snake(start=center, length=3, direction=(1, 0))
        self.food = Food.spawn(self.snake.occupies())
        self.score = 0
        self.direction = (1, 0)
        self._accumulator = 0.0

    def handle_event(self, event: pygame.event.Event) -> Optional[str]:
        if input_mod.read_pause_toggle(event):
            return "pause"
        new_dir = input_mod.read_direction_change(event, self.direction)
        if new_dir is not None:
            self.direction = new_dir
        return None

    def update(self) -> Optional[str]:
        # Move snake once per tick
        self.snake.set_direction(self.direction)
        self.snake.move()

        # Check food
        if self.snake.head() == self.food.position:
            self.snake.grow(1)
            self.score += 1
            self.food = Food.spawn(self.snake.occupies())

        # Check self-collision
        if self.snake.is_self_collision():
            return "game_over"
        return None

    def render(self, surface: pygame.Surface) -> None:
        ui.draw_grid(surface)
        ui.draw_food(surface, self.food.position)
        ui.draw_snake(surface, self.snake.occupies())
        # Score-only HUD retained; extended stats can be drawn by Game with player context
        ui.draw_score(surface, self.score)


