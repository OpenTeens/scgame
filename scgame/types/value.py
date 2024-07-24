class Value:
    def __init__(self, value):
        self._value = None
        self.value = value  # Use the setter for initial value validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, (bool, int, float, str)):
            raise TypeError("Value must be of type bool, int, float, or str.")
        self._value = new_value

    def __str__(self):
        return f"Value({self.value})"

    def __repr__(self):
        return f"Value({self.value!r})"