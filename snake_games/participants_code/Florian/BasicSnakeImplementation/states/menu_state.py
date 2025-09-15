from __future__ import annotations

from typing import Optional

import pygame

from .. import config
from .. import ui
from .. import input as input_mod


class MenuState:
    def __init__(self) -> None:
        self.selection_index = 0
        self.items = ["Start", "Quit"]  # Options placeholder to be added later

    def handle_event(self, event: pygame.event.Event) -> Optional[str]:
        if input_mod.read_confirm(event):
            if self.items[self.selection_index] == "Start":
                return "start"
            if self.items[self.selection_index] == "Quit":
                return "quit"

        if event.type == pygame.KEYDOWN:
            if event.key in config.KEY_UP:
                self.selection_index = (self.selection_index - 1) % len(self.items)
            elif event.key in config.KEY_DOWN:
                self.selection_index = (self.selection_index + 1) % len(self.items)
        return None

    def update(self) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        ui.draw_grid(surface)
        ui.draw_text_center(surface, "Snake", 48, 150)

        start_y = 320
        for idx, label in enumerate(self.items):
            prefix = "> " if idx == self.selection_index else "  "
            ui.draw_text_center(surface, f"{prefix}{label}", 32, start_y + idx * 40)


