import math
from scgame.sprite.base_sprite import BaseSprite
from scgame.utils import deg2rad

class MotionMixin(BaseSprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def move_forward(self, steps):
        """
        向前移动
        :param steps: 要移动的步数
        :return: None
        """
        delta_x = steps * math.sin(deg2rad(self.direction))
        delta_y = steps * math.cos(deg2rad(self.direction))
        self.x += delta_x
        self.y += delta_y
        self.game.refresh()

    def turn(self, degrees):
        """
        旋转精灵
        :param degrees: 要旋转的角度（度）
        :return: None
        """
        self.direction = (self.direction + degrees) % 360
        self.game.refresh()

    def go_to(self, x, y, seconds=0):
        """
        移动到指定位置
        :param x: 目标x坐标
        :param y: 目标y坐标
        :param seconds: 移动时间，默认为0（立即移动）
        :return: None
        """
        if seconds > 0:
            # 如果指定了时间，可以实现平滑移动的效果，这里简化为立即移动
            steps = int(math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2))
            self.move_forward(steps)
        else:
            self.x = x
            self.y = y
        self.game.refresh()

    def bounce(self, edge):
        """
        碰撞边界时的反弹效果
        :param edge: 碰撞的边界
        :return: None
        """
        if edge == 'top' or edge == 'bottom':
            self.direction = 180 - self.direction
        elif edge == 'left' or edge == 'right':
            self.direction = 360 - self.direction
        self.game.refresh()

    # TODO self.rotation_mode
