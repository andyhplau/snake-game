import constants
from direction import Direction
from drawable import Drawable
from food import Food
from segments import Segments
from pygame import draw, Surface


class AutoPilot(Drawable):
    """
    Represents the auto pilot of the snake. It is responsible for finding the path to the food.

    :attr _screen: the screen of the game
    :attr _is_active: True if the auto pilot is active, False otherwise
    :attr _segments: the segments of the snake
    :attr _final_path: the final path to the food
    :attr _visited: the visited segments
    """

    def __init__(self, segments: Segments, screen: Surface):
        """
        Initializes the auto pilot.

        :param segments: the segments of the snake
        """
        self._screen: Surface = screen
        self._is_active: bool = False
        self._segments: Segments = segments
        self._final_path: list[dict] = []
        self._visited: list[dict] = []

    def get_screen(self):
        return self._screen

    def get_is_active(self):
        return self._is_active

    def get_segments(self):
        return self._segments

    def get_final_path(self):
        return self._final_path

    def get_visited(self):
        return self._visited

    def switch_active(self):
        """
        Switches the state of the auto pilot.
        """
        self._is_active = not self._is_active

    def find_path(self, food: Food):
        """
        Finds the path to the food.

        :param food: the food
        :return: the path to the food or None if the path is not found
        """
        # implement the BFS algorithm
        queue: list[set] = []  # queue
        visited: list[dict] = []  # set

        path_to_the_head = [self._segments.get_segments_head()]
        queue.append((self._segments.get_segments_head(), path_to_the_head))

        while queue:
            segment, path = queue.pop(0)
            if segment == food.get_location():
                self._final_path = path
                self._visited = visited
                return path

            neighbors = self._find_neighbors(segment)
            valid_neighbors = self._find_valid_neighbors(neighbors)

            for neighbor in valid_neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def _find_neighbors(self, segment: list[dict]):
        """
        Finds the neighbors of the segment.

        :param segment: the segment
        :return: the neighbors of the segment
        """
        neigbors = []
        if segment["x"] < (constants.SCREEN_WIDTH - constants.BLOCK_SIZE):
            neigbors.append(
                {"x": segment["x"] + constants.BLOCK_SIZE, "y": segment["y"]}
            )
        if segment["x"] > 0:
            neigbors.append(
                {"x": segment["x"] - constants.BLOCK_SIZE, "y": segment["y"]}
            )
        if segment["y"] < (constants.SCREEN_HEIGHT - constants.BLOCK_SIZE):
            neigbors.append(
                {"x": segment["x"], "y": segment["y"] + constants.BLOCK_SIZE}
            )
        if segment["y"] > 0:
            neigbors.append(
                {"x": segment["x"], "y": segment["y"] - constants.BLOCK_SIZE}
            )
        return neigbors

    def _find_valid_neighbors(self, neighbors: list[dict]):
        """
        Finds the valid neighbors.

        :param neighbors: the neighbors
        :return: the valid neighbors
        """
        valid_neighbors = []
        for neighbor in neighbors:
            if neighbor not in self._segments.get_segments():
                valid_neighbors.append(neighbor)
        return valid_neighbors

    def draw(self):
        """
        Draws the visited segments and the final path.
        """
        # draw the visited segments
        if self._is_active:
            for segment in self._visited:
                draw.rect(
                    self._screen,
                    constants.VISITED_COLOR,
                    (
                        segment["x"],
                        segment["y"],
                        constants.BLOCK_SIZE,
                        constants.BLOCK_SIZE,
                    ),
                )

        # draw the final path
        if self._is_active:
            for segment in self._final_path:
                draw.rect(
                    self._screen,
                    constants.PATH_COLOR,
                    (
                        segment["x"],
                        segment["y"],
                        constants.BLOCK_SIZE,
                        constants.BLOCK_SIZE,
                    ),
                    2,
                )

    def __repr__(self):
        return f"segments: {self._segments}, screen: {self._screen})"
