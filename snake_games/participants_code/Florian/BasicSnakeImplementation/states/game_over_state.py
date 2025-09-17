from __future__ import annotations

from typing import Optional

import pygame

from .. import ui
from .. import storage
from .. import input as input_mod


class GameOverState:
    def __init__(self, score: int) -> None:
        self.score = score
        self.entries = [e.__dict__ for e in storage.load_highscores()]

    def handle_event(self, event: pygame.event.Event) -> Optional[str]:
        if input_mod.read_restart(event):
            return "restart"
        if input_mod.read_confirm(event):
            return "menu"
        if input_mod.read_back(event):
            return "menu"
        return None

    def update(self) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        ui.draw_overlay(surface)
        ui.draw_text_center(surface, "Game Over", 48, 260)
        ui.draw_text_center(surface, f"Score: {self.score}", 32, 320)
        ui.draw_text_center(surface, "Press R to Restart (same settings) or Enter for Menu", 24, 360)
        ui.draw_text_center(surface, "Highscores", 26, 400)
        ui.draw_highscores(surface, self.entries, start_y=430)


