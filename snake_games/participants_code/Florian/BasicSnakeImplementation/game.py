from __future__ import annotations

from typing import Optional

import pygame

from . import config
from .states.menu_state import MenuState
from .states.play_state import PlayState
from .states.pause_state import PauseState
from .states.game_over_state import GameOverState
from .states.setup_state import SetupState
from . import storage
from . import ui
import os


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self._init_audio()

        self.state: str = "setup"
        self.setup = SetupState()
        self.menu = MenuState()
        self.play: Optional[PlayState] = None
        self.pause = PauseState()
        self.game_over: Optional[GameOverState] = None
        self.player_name: str = "Player"
        self.fps: int = config.FPS

    def start_new_game(self) -> None:
        self.play = PlayState()
        self.state = "play"

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

                # State-specific event handling
                if self.state == "setup":
                    result = self.setup.handle_event(event)
                    if result is not None:
                        signal, data = result
                        if signal == "done":
                            self.player_name = data["name"]
                            self.fps = int(data["fps"]) or config.FPS
                            self.state = "menu"
                elif self.state == "menu":
                    result = self.menu.handle_event(event)
                    if result == "start":
                        self.start_new_game()
                    elif result == "quit":
                        running = False
                        break
                elif self.state == "play" and self.play is not None:
                    result = self.play.handle_event(event)
                    if result == "pause":
                        self.state = "pause"
                elif self.state == "pause":
                    result = self.pause.handle_event(event)
                    if result == "resume":
                        self.state = "play"
                    elif result == "menu":
                        self.state = "menu"
                elif self.state == "game_over" and self.game_over is not None:
                    result = self.game_over.handle_event(event)
                    if result == "restart":
                        self.start_new_game()
                    elif result == "menu":
                        self.state = "menu"

            # Update
            if self.state == "play" and self.play is not None:
                outcome = self.play.update()
                if outcome == "game_over":
                    score = self.play.score
                    # Persist score
                    storage.add_score(self.player_name, score, self.fps)
                    self.game_over = GameOverState(score)
                    self.state = "game_over"

            # Render
            if self.state == "setup":
                self.setup.render(self.screen)
            elif self.state == "menu":
                self.menu.render(self.screen)
            elif self.state == "play" and self.play is not None:
                self.play.render(self.screen)
                ui.draw_stats(self.screen, self.player_name, self.fps, self.play.score)
            elif self.state == "pause":
                # Render play underlay if exists
                if self.play is not None:
                    self.play.render(self.screen)
                    ui.draw_stats(self.screen, self.player_name, self.fps, self.play.score)
                self.pause.render(self.screen)
            elif self.state == "game_over" and self.game_over is not None:
                # Render play underlay if exists
                if self.play is not None:
                    self.play.render(self.screen)
                self.game_over.render(self.screen)

            pygame.display.flip()
            # Fixed tick rate for gameplay feel; menu/pause use same rate for simplicity
            self.clock.tick(self.fps if self.state in {"play", "pause", "menu"} else config.FPS)

        pygame.quit()

    def _init_audio(self) -> None:
        if not config.ENABLE_MUSIC:
            return
        try:
            pygame.mixer.init()
            if os.path.exists(config.BGM_FILE):
                pygame.mixer.music.load(config.BGM_FILE)
                pygame.mixer.music.set_volume(config.BGM_VOLUME)
                pygame.mixer.music.play(loops=-1)
        except Exception:
            # Gracefully ignore audio errors
            pass


