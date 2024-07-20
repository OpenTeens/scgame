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

    def point_towards(self, target):
        if type(target) == int:
            self.direction = target
        else:
            self.direction = arctan((target.x - self.x) / (target.y - self.y))
            if target.y < self.y:
                self.direction += 180
            elif target.x < self.x and target.y > self.y:
                self.direction += 360
    
    def on_edge(self) -> bool:
        return not(-240 <= self.x <= 240 and -180 <= self.y <= 180)