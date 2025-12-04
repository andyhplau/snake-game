import constants
import pygame
from drawable import Drawable


class Score(Drawable):
    """
    Represents the score keeper.

    :attr _screen: the screen of the game
    :attr _score: the score of the game
    """

    def __init__(self, screen: pygame.Surface):
        """
        Initializes the score keeper.

        :param screen: the screen of the game
        """
        self._screen: pygame.Surface = screen
        self._score = 0

    def get_screen(self):
        return self._screen

    def get_score(self):
        return self._score

    def set_score(self, score: int):
        self._score = score

    def increase_score(self):
        """
        Increases the score by 1.
        """
        self._score += 1

    def reset_score(self):
        """
        Resets the score to 0.
        """
        self._score = 0

    def draw(self):
        """
        Draw the score on the screen.
        """
        font = pygame.font.Font(None, 35)
        text = font.render(f"Score: {self._score}", True, constants.WHITE)
        self._screen.blit(
            text,
            (
                constants.SCREEN_WIDTH - 1.5 * text.get_width(),
                text.get_height(),
            ),
        )

    def __repr__(self) -> str:
        return f"screen: {self._screen}, score: {self._score}"
