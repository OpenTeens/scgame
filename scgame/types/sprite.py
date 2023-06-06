from typing import List, Dict


class Sprite:
    def __init__(self, name: str, visible: bool, current_costume: int, costumes: List[Dict], sounds: List, volume: int,
                 layer_order: int, x: int, y: int, size: int, direction: int,
                 draggable: bool, rotation_style: str, global_vars: Dict, global_lists: Dict[str, List]):
        self.name = name
        self.visible = visible
        self.current_costume = current_costume
        self.costumes = costumes
        self.sounds = sounds
        self.volume = volume
        self.layer_order = layer_order
        self.x = x
        self.y = y
        self.size = size
        self.direction = direction
        self.draggable = draggable
        self.rotation_style = rotation_style
        self.global_vars = global_vars
        self.global_lists = global_lists
        self.local_vars = dict()
        self.local_lists: Dict[str, List] = dict()

    def when_greenflag_clicked(self):
        pass

    def when_key_pressed(self, key: str):
        pass

    def when_this_sprite_clicked(self):
        pass

    def when_backdrop_switches_to(self, background: str):
        pass

    def when_broadcast(self, broadcast: str):
        pass
