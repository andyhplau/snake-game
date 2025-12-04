import constants
from direction import Direction


class Segments:
    """
    Represents the segments of the snake.

    :attr _segments: the segments of the snake
    """

    def __init__(self, length: int, x: int, y: int):
        """
        Initializes the segments of the snake.

        :param length: the length of the snake
        :param x: the x-coordinate of the tail of the snake
        :param y: the y-coordinate of the tail of the snake
        """
        self._segments: list[dict] = []
        for i in range(length):
            self._segments.append({"x": x + i * constants.BLOCK_SIZE, "y": y})

    def get_segments(self):
        return self._segments

    def get_segments_length(self):
        """
        Get the length of the segments of the snake.

        :return: the length of the segments of the snake
        """
        return len(self._segments)

    def get_segments_head(self):
        """
        Get the head segment of the snake.

        :return: the head segment of the snake
        """
        return self._segments[-1]

    def update_segments_body(self, index: int):
        """
        Update the body of the snake.

        :param index: the index of the segment
        """
        self._segments[index]["x"] = self._segments[index + 1]["x"]
        self._segments[index]["y"] = self._segments[index + 1]["y"]

    def update_segments_head(self, direction: Direction):
        """
        Update the head segment of the snake.

        :param direction: the direction of the snake
        """
        if direction == Direction.UP:
            self._segments[-1]["y"] -= constants.BLOCK_SIZE
        elif direction == Direction.DOWN:
            self._segments[-1]["y"] += constants.BLOCK_SIZE
        elif direction == Direction.LEFT:
            self._segments[-1]["x"] -= constants.BLOCK_SIZE
        elif direction == Direction.RIGHT:
            self._segments[-1]["x"] += constants.BLOCK_SIZE

    def add_segment(self, direction: Direction):
        """
        Add a segment to the snake.

        :param direction: the direction of the snake
        """
        if direction == Direction.UP:
            self._segments.append(
                {
                    "x": self._segments[-1]["x"],
                    "y": self._segments[-1]["y"] - constants.BLOCK_SIZE,
                }
            )
        elif direction == Direction.DOWN:
            self._segments.append(
                {
                    "x": self._segments[-1]["x"],
                    "y": self._segments[-1]["y"] + constants.BLOCK_SIZE,
                }
            )
        elif direction == Direction.LEFT:
            self._segments.append(
                {
                    "x": self._segments[-1]["x"] - constants.BLOCK_SIZE,
                    "y": self._segments[-1]["y"],
                }
            )
        elif direction == Direction.RIGHT:
            self._segments.append(
                {
                    "x": self._segments[-1]["x"] + constants.BLOCK_SIZE,
                    "y": self._segments[-1]["y"],
                }
            )

    def __repr__(self):
        return f"segments: {self._segments}"
