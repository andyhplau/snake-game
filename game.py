import constants
import random
import pygame
from direction import Direction
from drawable import Drawable
from food import Food
from score import Score
from snake import Snake


class Game(Drawable):
    """
    Represents the Snake game.

    :attr _screen: the screen of the game
    :attr _score: the score of the game
    :attr _snake: the snake
    :attr _food: the food
    """

    def __init__(self):
        """
        Initializes the game.
        """
        pygame.init()
        self._screen: pygame.Surface = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(constants.GAME_NAME)
        self._screen.fill(constants.BLACK)
        self._score: Score = Score(self._screen)
        self._snake: Snake = Snake(
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2,
            self._screen,
        )
        # randomize the food location
        food_location = [
            constants.SCREEN_WIDTH / 4,
            constants.SCREEN_HEIGHT / 4 * 3,
        ]
        self._food: Food = Food(
            food_location[random.randint(0, 1)],
            food_location[random.randint(0, 1)],
            self._screen,
        )

    def get_screen(self):
        return self._screen

    def get_score(self):
        return self._score

    def get_snake(self):
        return self._snake

    def get_food(self):
        return self._food

    def start(self):
        """
        Starts the game.
        """
        # the game loop
        clock = pygame.time.Clock()
        running = True
        pause = False
        while running:
            clock.tick(constants.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if not pause:
                        if event.key == pygame.K_UP:
                            self._snake._direction = Direction.UP
                        elif event.key == pygame.K_DOWN:
                            self._snake._direction = Direction.DOWN
                        elif event.key == pygame.K_LEFT:
                            self._snake._direction = Direction.LEFT
                        elif event.key == pygame.K_RIGHT:
                            self._snake._direction = Direction.RIGHT
                        elif event.key == pygame.K_a:
                            auto_pilot = self._snake.get_auto_pilot()
                            auto_pilot.switch_active()
                    else:
                        if event.key == pygame.K_SPACE:
                            pause = False
                            self._snake = Snake(
                                constants.SCREEN_WIDTH / 2,
                                constants.SCREEN_HEIGHT / 2,
                                self._screen,
                            )
            try:
                if not pause:
                    self.update()
                    self.draw()
            except Exception as e:
                pause = True
                self._score.reset_score()
                self.game_over(str(e))

    def update(self):
        """
        Updates the game.
        """
        self._snake.update(self._food, self._score)

    def draw(self):
        """
        Draws the elements of the game and display them.
        """
        self._screen.fill(constants.BLACK)
        self._snake.draw()
        self._food.draw()
        self._score.draw()
        pygame.display.flip()

    def game_over(self, message: str):
        """
        Displays the game over message.

        :param message: the game over message to display
        """
        self._screen.fill(constants.BLACK)
        font = pygame.font.Font(None, 35)
        text = font.render(message + " Hit Space to restart!", True, constants.RED)
        self._screen.blit(
            text,
            (
                (constants.SCREEN_WIDTH - text.get_width()) / 2,
                (constants.SCREEN_HEIGHT - text.get_height()) / 2,
            ),
        )
        pygame.display.flip()

    def __repr__(self):
        return f"screen: {self._screen}, score: {self._score}, snake: {self._snake}, food: {self._food})"
