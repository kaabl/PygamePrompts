from __future__ import annotations

from typing import Optional, Tuple

import pygame

from . import config

Direction = Tuple[int, int]

# Cardinal directions
UP: Direction = (0, -1)
DOWN: Direction = (0, 1)
LEFT: Direction = (-1, 0)
RIGHT: Direction = (1, 0)


def is_reverse(a: Direction, b: Direction) -> bool:
    return a[0] == -b[0] and a[1] == -b[1]


def read_direction_change(event: pygame.event.Event, current: Direction) -> Optional[Direction]:
    """Return a new direction if a valid key is pressed, else None.

    Prevent reversing directly into the snake's body.
    """
    if event.type != pygame.KEYDOWN:
        return None

    key = event.key
    if key in config.KEY_UP and not is_reverse(current, UP):
        return UP
    if key in config.KEY_DOWN and not is_reverse(current, DOWN):
        return DOWN
    if key in config.KEY_LEFT and not is_reverse(current, LEFT):
        return LEFT
    if key in config.KEY_RIGHT and not is_reverse(current, RIGHT):
        return RIGHT
    return None


def read_pause_toggle(event: pygame.event.Event) -> bool:
    return event.type == pygame.KEYDOWN and event.key in config.KEY_PAUSE


def read_confirm(event: pygame.event.Event) -> bool:
    return event.type == pygame.KEYDOWN and event.key in config.KEY_CONFIRM


def read_back(event: pygame.event.Event) -> bool:
    return event.type == pygame.KEYDOWN and event.key in config.KEY_BACK


def read_restart(event: pygame.event.Event) -> bool:
    return event.type == pygame.KEYDOWN and event.key in config.KEY_RESTART


