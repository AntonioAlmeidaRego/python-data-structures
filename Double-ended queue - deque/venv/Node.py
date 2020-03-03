class Node:
    def __init__(self):
        self._value = 0;
        self._key = 0;
        self._ant = Node;
        self._prox = Node;

    def get_value(self):
        return self._value;
    def set_value(self, value):
        self._value = value;
    def get_key(self):
        return self._key;
    def set_key(self, key):
        self._key = key;
    def get_ant(self):
        return self._ant;
    def set_ant(self, ant):
        self._ant = ant;
    def get_prox(self):
        return self._prox;
    def set_prox(self, prox):
        self._prox = prox;

