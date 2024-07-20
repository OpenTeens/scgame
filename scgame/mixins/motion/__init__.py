import math
from scgame.sprite.base_sprite import BaseSprite
from scgame.utils import deg2rad


class MotionMixin(BaseSprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = 0  # 默认速度设置为0

    def move_forward(self, distance=None):
        """
        向前移动
        :param distance: 要移动的距离。如果为None，则使用当前速度。
        :return: None
        """
        if distance is None:
            distance = self.speed
        delta_x = distance * math.sin(deg2rad(self.direction))
        delta_y = distance * math.cos(deg2rad(self.direction))
        self.x += delta_x
        self.y += delta_y
        self.game.refresh()

    def rotate(self, angle):
        """
        旋转精灵
        :param angle: 要旋转的角度（度）。
        :return: None
        """
        self.direction = (self.direction + angle) % 360
        self.game.refresh()

    def stop(self):
        """
        停止精灵移动，将速度设置为0
        :return: None
        """
        self.speed = 0

    def move_backward(self, distance=None):
        """
        向后移动
        :param distance: 要移动的距离。如果为None，则使用当前速度。
        :return: None
        """
        if distance is None:
            distance = self.speed
        delta_x = -distance * math.sin(deg2rad(self.direction))
        delta_y = -distance * math.cos(deg2rad(self.direction))
        self.x += delta_x
        self.y += delta_y
        self.game.refresh()