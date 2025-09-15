from __future__ import annotations

from typing import Optional, Tuple

import pygame

from .. import ui
from .. import config


class SetupState:
    def __init__(self) -> None:
        self.name = ""
        self.speeds = [10, 12, 15]
        self.speed_index = 0
        self.mode: str = "name"  # or "speed"

    def handle_event(self, event: pygame.event.Event) -> Optional[Tuple[str, dict]]:
        if event.type == pygame.KEYDOWN:
            if self.mode == "name":
                if event.key == pygame.K_RETURN:
                    self.mode = "speed"
                elif event.key == pygame.K_BACKSPACE:
                    self.name = self.name[:-1]
                else:
                    # Add printable characters (basic filter)
                    ch = event.unicode
                    if ch.isprintable() and not ch.isspace() and len(self.name) < 12:
                        self.name += ch
            elif self.mode == "speed":
                if event.key in config.KEY_LEFT:
                    self.speed_index = (self.speed_index - 1) % len(self.speeds)
                elif event.key in config.KEY_RIGHT:
                    self.speed_index = (self.speed_index + 1) % len(self.speeds)
                elif event.key in config.KEY_CONFIRM:
                    # Done
                    name = self.name or "Player"
                    return (
                        "done",
                        {"name": name, "fps": self.speeds[self.speed_index]},
                    )
        return None

    def update(self) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        ui.draw_grid(surface)
        ui.draw_text_center(surface, "Setup", 40, 120)

        ui.draw_text_center(
            surface,
            "Enter Name (Enter to confirm):",
            24,
            220,
        )
        ui.draw_text_center(surface, self.name or "_", 32, 260)

        ui.draw_text_center(surface, "Select Speed (Enter to confirm):", 24, 340)
        s = self.speeds[self.speed_index]
        ui.draw_text_center(surface, f"{s} FPS", 32, 380)

        # Indicate focus
        if self.mode == "name":
            ui.draw_text_center(surface, "[Typing Name]", 18, 300)
        else:
            ui.draw_text_center(surface, "[Choosing Speed with Left/Right]", 18, 420)


