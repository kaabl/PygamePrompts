from __future__ import annotations

from typing import Optional

import pygame

from .. import ui
from .. import input as input_mod


class PauseState:
    def __init__(self) -> None:
        self.items = ["Resume", "Quit to Menu"]
        self.selection_index = 0

    def handle_event(self, event: pygame.event.Event) -> Optional[str]:
        if input_mod.read_confirm(event):
            if self.selection_index == 0:
                return "resume"
            return "menu"

        if event.type == pygame.KEYDOWN:
            # Reuse up/down sets from config via input module checks
            from .. import config

            if event.key in config.KEY_UP:
                self.selection_index = (self.selection_index - 1) % len(self.items)
            elif event.key in config.KEY_DOWN:
                self.selection_index = (self.selection_index + 1) % len(self.items)

        if input_mod.read_back(event) or input_mod.read_pause_toggle(event):
            return "resume"
        return None

    def update(self) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        ui.draw_overlay(surface)
        ui.draw_text_center(surface, "Paused", 44, 260)
        start_y = 340
        for idx, label in enumerate(self.items):
            prefix = "> " if idx == self.selection_index else "  "
            ui.draw_text_center(surface, f"{prefix}{label}", 28, start_y + idx * 36)


