from abc import abstractmethod
from typing import Union

import pygame


class Game(object):
    """A class with all the main attributes of the game (game window)"""
    caption: str
    width: int
    height: int
    icon: str  # path to image
    framerate: Union[int, float]

    def __init__(self, caption, width, height, icon, framerate=60):
        pygame.init()
        pygame.display.set_caption(caption)
        pygame.display.set_icon(pygame.image.load(icon))
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.framerate = framerate
        self.width = width
        self.height = height
        self.game_over = False

    @abstractmethod
    def update(self) -> None:
        """Updating the game status"""
        pass

    @abstractmethod
    def handle_events(self) -> None:
        """Handles actions entered by the player"""
        pass

    @abstractmethod
    def restart(self) -> None:
        """Launches a new game"""
        pass

    def run(self) -> None:
        """Launches the game"""
        pass