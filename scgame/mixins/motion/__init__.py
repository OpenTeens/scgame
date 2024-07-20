import math

from scgame.sprite.base_sprite import BaseSprite
from scgame.utils import deg2rad


class MotionMixin(BaseSprite):
    def move_forward(self, distance):
        """
        Move forward.
        :param distance: distance to move
        :return: None
        """
        delta_x = distance * math.sin(deg2rad(self.direction))
        delta_y = distance * math.cos(deg2rad(self.direction))
        self.x += delta_x
        self.y += delta_y
        self.game.refresh()
