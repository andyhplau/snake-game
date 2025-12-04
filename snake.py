from auto_pilot import AutoPilot
import constants
from pygame import Surface, draw
from direction import Direction
from drawable import Drawable
from food import Food
from score import Score
from segments import Segments


class Snake(Drawable):
    """
    Represents the snake.

    :attr _screen: the screen of the game
    :attr _direction: the direction of the snake
    :attr _segments: the segments of the snake
    :attr _auto_pilot: the auto pilot of the snake
    """

    def __init__(self, x: int, y: int, screen: Surface):
        """
        Initializes the snake.

        :param x: the x-coordinate of the snake
        :param y: the y-coordinate of the snake
        :param screen: the screen of the game
        """
        self._screen: Surface = screen
        self._direction: Direction = Direction.RIGHT
        self._segments: Segments = Segments(4, x, y)
        self._auto_pilot: AutoPilot = AutoPilot(self._segments, self._screen)

    def get_screen(self):
        return self._screen

    def get_direction(self):
        return self._direction

    def get_segments(self):
        return self._segments

    def get_auto_pilot(self):
        return self._auto_pilot

    def draw(self):
        """
        Draw the snake on the screen.
        """
        self._auto_pilot.draw()
        # draw the snake segments
        for segment in self._segments.get_segments():
            draw.rect(
                self._screen,
                constants.WHITE,
                (
                    segment["x"],
                    segment["y"],
                    constants.BLOCK_SIZE,
                    constants.BLOCK_SIZE,
                ),
            )

    def update(self, food: Food, score: Score):
        """
        Update the snake.

        :param food: the food
        :param score: the score
        """
        # update the body of the snake
        for i in range(self._segments.get_segments_length() - 1):
            self._segments.update_segments_body(i)

        if self._auto_pilot.get_is_active():
            path = self._auto_pilot.find_path(food)
            if path[1]["x"] > path[0]["x"]:
                self._direction = Direction.RIGHT
            elif path[1]["x"] < path[0]["x"]:
                self._direction = Direction.LEFT
            elif path[1]["y"] > path[0]["y"]:
                self._direction = Direction.DOWN
            elif path[1]["y"] < path[0]["y"]:
                self._direction = Direction.UP

        # update the head of the snake
        self._segments.update_segments_head(self._direction)

        # check if the snake has eaten the food
        if self.is_collided_with_food(food):
            self.increase_size_by_one()
            food.change_location(self._segments)
            score.increase_score()

        # check if the snake is collided with walls
        if self.is_collided_with_walls():
            raise HitWallError("Game Over! Collided with walls!")

        # check if the snake is collided with itself
        if self.is_collided_with_itself():
            raise HitItselfError("Game Over! Collided with itself!")

    def is_collided_with_food(self, food: Food):
        """
        Check if the snake has eaten the food.

        :param food: the food
        :return: True if the snake has eaten the food, False otherwise
        """
        return (
            self._segments.get_segments_head()["x"] == food._x
            and self._segments.get_segments_head()["y"] == food._y
        )

    def increase_size_by_one(self):
        """
        Increase the size of the snake by one.
        """
        # detect the direct of the snake
        self._segments.add_segment(self._direction)

    def is_collided_with_walls(self):
        """
        Check if the snake is collided with walls.

        :return: True if the snake is collided with walls, False otherwise
        """
        return (
            self._segments.get_segments_head()["x"] < 0
            or self._segments.get_segments_head()["x"]
            > (constants.SCREEN_WIDTH - constants.BLOCK_SIZE)
            or self._segments.get_segments_head()["y"] < 0
            or self._segments.get_segments_head()["y"]
            > (constants.SCREEN_HEIGHT - constants.BLOCK_SIZE)
        )

    def is_collided_with_itself(self):
        """
        Check if the snake is collided with itself.

        :return: True if the snake is collided with itself, False otherwise
        """
        return self._segments.get_segments_head() in self._segments.get_segments()[:-1]

    def __repr__(self):
        return f"screen: {self._screen}, direction: {self._direction}, segments: {self._segments}, auto_pilot: {self._auto_pilot}"


class HitWallError(Exception):
    """
    Represents the error when the snake is collided with walls.
    """

    def __init__(self, message):
        """
        Initializes the error.
        """
        super().__init__(message)


class HitItselfError(Exception):
    """
    Represents the error when the snake is collided with itself.
    """

    def __init__(self, message):
        """
        Initializes the error.
        """
        super().__init__(message)
