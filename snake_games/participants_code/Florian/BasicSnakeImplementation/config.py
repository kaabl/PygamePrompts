from __future__ import annotations

import os
import pygame

# Grid configuration
GRID_COLS = 30
GRID_ROWS = 30
CELL_SIZE = 25  # pixels

# Derived window size
WINDOW_WIDTH = GRID_COLS * CELL_SIZE
WINDOW_HEIGHT = GRID_ROWS * CELL_SIZE

# Timing
FPS = 10  # game tick rate for movement/updates

# Colors (R, G, B)
COLOR_BG = (18, 18, 18)
COLOR_GRID = (40, 40, 40)
COLOR_SNAKE_HEAD = (80, 200, 120)
COLOR_SNAKE_BODY = (60, 170, 100)
COLOR_FOOD = (220, 80, 80)
COLOR_TEXT = (230, 230, 230)
COLOR_OVERLAY = (0, 0, 0, 120)

# Input bindings
KEY_UP = {pygame.K_UP, pygame.K_w}
KEY_DOWN = {pygame.K_DOWN, pygame.K_s}
KEY_LEFT = {pygame.K_LEFT, pygame.K_a}
KEY_RIGHT = {pygame.K_RIGHT, pygame.K_d}
KEY_PAUSE = {pygame.K_p}
KEY_CONFIRM = {pygame.K_RETURN, pygame.K_SPACE}
KEY_BACK = {pygame.K_ESCAPE}
KEY_RESTART = {pygame.K_r}

# Behavior
WRAP_AROUND = True

# Audio
ENABLE_MUSIC = False
BGM_FILE = os.path.join(os.path.dirname(__file__), "assets", "bgm.ogg")
BGM_VOLUME = 0.4  # 0.0 - 1.0


