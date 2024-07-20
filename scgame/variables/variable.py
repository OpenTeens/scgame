class ScVariable:
    def __init__(self, name):
        self.name = name
        self.val = 0
    
    def set_value(self, val):
        self.val = val
    
    def increment(self, inc):
        if not isinstance(self.val, (int, float)):
            self.val = 0
        self.val += inc


def data_setvariableto(variable: ScVariable, val):
    variable.set_value(val)

def data_changevariableby(variable: ScVariable, inc: int):
    variable.increment(inc)
