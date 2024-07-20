import math
import pygame

from scgame.game import Game
from scgame.utils import deg2rad


class BaseSprite:
    def __init__(self):
        self.name = ""
        self.visible = True
        self.current_costume = 0
        self.costumes = []
        self.sounds = []
        self.volume = []
        self.layer_order = 0
        self.x = 0
        self.y = 0
        self.size = 100
        self.direction = 90
        self.draggable = True
        self.rotation_style = ""  # "all around" | "left-right" | "don't rotate"
        self.global_vars = dict()
        self.global_lists: dict[str, list] = dict()
        self.local_vars = dict()
        self.local_lists: dict[str, list] = dict()
        self.game: Game | None = None

    def set_game(self, game: Game):
        self.game = game
        self.global_vars = game.global_vars
        self.global_lists = game.global_lists

    def render(self, screen: pygame.Surface):
        # 新建一个sprite对象
        sprite = pygame.sprite.Sprite()
        sprite.image = self.costumes[self.current_costume]
        sprite.rect = sprite.image.get_rect()
        sprite.rect.center = (self.x, self.y)
        screen.blit(sprite.image, sprite.rect)
