from scgame.types import value

def add(a, b):
    return value.Value(a.value + b.value)

def sub(a, b):
    return value.Value(a.value - b.value)

def mul(a, b):
    return value.Value(a.value * b.value)

def div(a, b):
    return value.Value(a.value / b.value)

#True if b > a, False otherwise
def compare(a, b):
    return value.Value(b.value > a.value)