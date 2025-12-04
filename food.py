import random
import constants
from pygame import Surface, draw
from drawable import Drawable
from segments import Segments


class Food(Drawable):
    """
    Represents the food of the snake.

    :attr _x: int: the x coordinate of the food
    :attr _y: int: the y coordinate of the food
    :attr _screen: the screen
    """

    def __init__(self, x: int, y: int, screen: Surface):
        """
        Initializes the food.

        :param x: the x coordinate of the food
        :param y: the y coordinate of the food
        :param screen: the screen
        """
        self._x: int = x
        self._y: int = y
        self._screen: Surface = screen

    def get_location(self):
        return {"x": self._x, "y": self._y}

    def get_screen(self):
        return self._screen

    def change_location(self, segments: Segments):
        """
        Changes the location of the food.

        :param segments: the segments of the snake
        """
        while True:
            x = (
                random.randint(
                    0, int(constants.SCREEN_WIDTH / constants.BLOCK_SIZE) - 1
                )
                * constants.BLOCK_SIZE
            )
            y = (
                random.randint(
                    0, int(constants.SCREEN_HEIGHT / constants.BLOCK_SIZE) - 1
                )
                * constants.BLOCK_SIZE
            )
            if {"x": x, "y": y} not in segments.get_segments():
                self._x = x
                self._y = y
                break

    def draw(self):
        """
        Draws the food.
        """
        draw.rect(
            self._screen,
            constants.FOOD_COLOR,
            (self._x, self._y, constants.BLOCK_SIZE, constants.BLOCK_SIZE),
        )

    def __repr__(self):
        return f"x: {self._x}, y: {self._y}, screen: {self._screen})"
