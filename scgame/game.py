import pygame
from typing import Dict, List
from typing import TYPE_CHECKING

from .events.base import BaseEvent
from .consts import *

if TYPE_CHECKING:
    from .sprite import Sprite


class Game:
    def __init__(
            self, 
            caption="SC Game", 
            size=(480, 360), 
            flags=HWSURFACE|DOUBLEBUF):
        self.global_vars = dict()
        self.global_lists: Dict[str, List] = dict()
        self.listeners: dict[BaseEvent, list[callable]] = dict()
        self.running = False
        self.refresh_required = True
        self.sprites: list[Sprite] = []

        self.screen = pygame.display.set_mode(size, flags)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(caption)

    def mainloop(self):
        pygame.init()
        self.running = True
        self.screen.fill(WHITE)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    break
                ...

            if not self.running:
                break

            if self.refresh_required:
                pygame.display.flip()
                self.refresh_required = False

        pygame.quit()

    def refresh(self):
        self.refresh_required = True
        self.clock.tick(30)

    def render_sprites(self):
        for sprite in self.sprites:
            sprite.render(self.screen)
            self.refresh()

    def add_sprite(self, sprite: "Sprite"):
        sprite.set_game(self)
        self.sprites.append(sprite)

    def add_listener(self, event: BaseEvent, listener: callable):
        self.listeners[event] = listener
