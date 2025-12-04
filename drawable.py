from abc import ABC, abstractmethod


class Drawable(ABC):
    """
    Interface for drawable objects
    """

    @abstractmethod
    def draw(self):
        """
        Draw the object
        """
        pass
