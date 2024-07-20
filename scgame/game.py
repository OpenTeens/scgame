import pygame
from typing import Dict, List
from typing import TYPE_CHECKING

from scgame.events.base import BaseEvent

if TYPE_CHECKING:
    from scgame.sprite import Sprite


class Game:
    def __init__(self):
        self.global_vars = dict()
        self.global_lists: Dict[str, List] = dict()
        self.listeners: dict[BaseEvent, list[callable]] = dict()
        self.running = False

        self.screen = pygame.display.set_mode((480, 360,))
        pygame.display.set_caption("SC Game")
        pygame.init()

    def mainloop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    break

            if not self.running:
                break

            pygame.display.flip()
        pygame.quit()

    def add_sprite(self, sprite: "Sprite"):
        pass

    def refresh(self):
        pass

    def add_listener(self, event: BaseEvent, listener: callable):
        pass
