class Node:

    def __init__(self):
        self._value = 0
        self._key = 0
        self._prox = None
        self._ant = None

    def __get_value__(self):
        return self._value

    def __set_value__(self, value):
        self._value = value

    def __set_key__(self, key):
        self._key = key

    def __get_key__(self):
        return self._key

    def __get_prox__(self):
        return self._prox

    def __set_prox__(self, prox):
        self._prox = prox

    def __set_ant__(self, ant):
        self._ant = ant

    def __get_ant__(self):
        return self._ant
