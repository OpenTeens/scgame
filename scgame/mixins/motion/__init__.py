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

    def point_towards(self, target):
        """
        精灵朝向特定目标
        :param target: 可以是具有x和y坐标的对象，或者是一个特定的角度（整数）
        :return: None
        """
        if isinstance(target, int):
            self.direction = target
        else:
            self.direction = math.degrees(math.atan2(target.x - self.x, target.y - self.y))
            if self.direction < 0:
                self.direction += 360
    
    def on_edge(self) -> bool:
        """
        检查精灵是否触碰到边界
        :return: 如果精灵触碰到边界，返回True，否则返回False
        """
        return not(-240 <= self.x <= 240 and -180 <= self.y <= 180)

    def go_to(self, x, y, secs = 0):
        """
        移动到指定位置
        :param x: 目标x坐标
        :param y: 目标y坐标
        :param secs: 移动时间，默认为0（立即移动）
        :return: None
        """
        if secs > 0:
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

        self.direction %= 360
        self.game.refresh()

    # TODO self.rotation_mode
    def set_rotation_mode(self, mode, limits=None):
        """
        设置旋转模式
        :param mode: 旋转模式 ('none', 'all', 'limited')
        :param limits: 旋转限制 (仅在模式为 'limited' 时使用), 为一个元组表示角度范围 (min, max)
        :return: None
        """
        self.rotation_mode = mode
        if mode == 'limited' and limits:
            self.rotation_limits = limits
        elif mode != 'limited':
            self.rotation_limits = None
