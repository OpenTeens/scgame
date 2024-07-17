import math
from typing import List, Dict

from scgame.game import Game


def deg2rad(deg):
    """
    [Tool]: Convert degree to radian.
    :param deg: degree
    :return: radian
    """
    return deg / 180 * math.pi


class Sprite:
    def __init__(self, game: Game):
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
        self.global_vars = game.global_vars
        self.global_lists = game.global_lists
        self.local_vars = dict()
        self.local_lists: Dict[str, List] = dict()

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
