from .variable import ScVariable

class ScVariableList:
    def __init__(self):
        self.variables = []

    def add_variable(self, name):
        variable = ScVariable(name)
        self.variables.append(variable)
        return variable

    def get_variable(self, name):
        for variable in self.variables:
            if variable.name == name:
                return variable
        return None

    def set_variable_value(self, name, val):
        variable = self.get_variable(name)
        if variable is not None:
            variable.set_value(val)

    def increment_variable(self, name, inc):
        variable = self.get_variable(name)
        if variable is not None:
            variable.increment(inc)