import sys

from .game import Game


def main() -> int:
    game = Game()
    game.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())


