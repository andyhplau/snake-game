from game import Game


class Driver:
    """
    Represents the driver class of the Snake Game.
    """

    @staticmethod
    def start():
        """
        Starts the game.
        """
        Game().start()


def main():
    Driver.start()


if __name__ == "__main__":
    main()
