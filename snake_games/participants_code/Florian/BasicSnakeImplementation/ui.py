from __future__ import annotations

from typing import Iterable, Tuple, List

import pygame

from . import config
from . import utils

GridPos = Tuple[int, int]


def draw_grid(surface: pygame.Surface) -> None:
    surface.fill(config.COLOR_BG)
    # Optional grid lines for clarity
    for x in range(config.GRID_COLS):
        for y in range(config.GRID_ROWS):
            rect = pygame.Rect(*utils.grid_to_pixel(x, y))
            pygame.draw.rect(surface, config.COLOR_GRID, rect, width=1)


def draw_snake(surface: pygame.Surface, body: Iterable[GridPos]) -> None:
    body_list = list(body)
    if not body_list:
        return
    # Head
    hx, hy = body_list[0]
    pygame.draw.rect(surface, config.COLOR_SNAKE_HEAD, pygame.Rect(*utils.grid_to_pixel(hx, hy)))
    # Body
    for (x, y) in body_list[1:]:
        pygame.draw.rect(surface, config.COLOR_SNAKE_BODY, pygame.Rect(*utils.grid_to_pixel(x, y)))


def draw_food(surface: pygame.Surface, position: GridPos) -> None:
    pygame.draw.rect(surface, config.COLOR_FOOD, pygame.Rect(*utils.grid_to_pixel(*position)))


def get_font(size: int) -> pygame.font.Font:
    return pygame.font.SysFont(None, size)


def draw_text_center(surface: pygame.Surface, text: str, size: int, y: int) -> None:
    font = get_font(size)
    surf = font.render(text, True, config.COLOR_TEXT)
    rect = surf.get_rect(center=(config.WINDOW_WIDTH // 2, y))
    surface.blit(surf, rect)


def draw_score(surface: pygame.Surface, score: int) -> None:
    font = get_font(24)
    text_surf = font.render(f"Score: {score}", True, config.COLOR_TEXT)
    surface.blit(text_surf, (10, 10))


def draw_overlay(surface: pygame.Surface) -> None:
    overlay = pygame.Surface((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill(config.COLOR_OVERLAY)
    surface.blit(overlay, (0, 0))


def draw_stats(surface: pygame.Surface, name: str, speed: int, score: int) -> None:
    font = get_font(24)
    text = f"Player: {name}  |  Speed: {speed}  |  Score: {score}"
    surf = font.render(text, True, config.COLOR_TEXT)
    rect = surf.get_rect()
    rect.topright = (config.WINDOW_WIDTH - 10, 10)
    surface.blit(surf, rect)


def draw_highscores(surface: pygame.Surface, entries: List[dict], start_y: int = 420) -> None:
    ui_font = get_font(22)
    y = start_y
    for idx, e in enumerate(entries[:10], start=1):
        line = f"{idx}. {e.get('name','?')}  —  {e.get('score',0)}  ({e.get('speed',0)} FPS)"
        surf = ui_font.render(line, True, config.COLOR_TEXT)
        rect = surf.get_rect(center=(config.WINDOW_WIDTH // 2, y))
        surface.blit(surf, rect)
        y += 28


