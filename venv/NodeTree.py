class NodeTree:
    def __init__(self):
        self._left = None
        self._right = None
        self._father = None
        self._value = 0

    def __get_value__(self):
        return self._value

    def __get_left__(self):
        return self._left

    def __get_right__(self):
        return self._right

    def __get_father__(self):
        return self._father

    def __set_value__(self, value):
        self._value = value

    def __set_left__(self, left):
        self._left = left

    def __set_right__(self, right):
        self._right = right

    def __set_father__(self, father):
        self._father = father
