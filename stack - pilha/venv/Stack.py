
from Node import Node


class Stack:
    def __init__(self):
        self._head = Node();
        self._syrup = Node();
        self._head.set_prox(self._syrup);
        self._head.set_ant(self._syrup);
        self._syrup.set_prox(self._head);
        self._syrup.set_ant(self._head);
        self._length = 0;

    def size(self):
        return self._length;

    def empty(self):
        if(self._head.get_prox() == self._syrup):
            return True;
        return False;

    def push(self, value, key):
        novo = Node();
        novo.set_key(key);
        novo.set_value(value);
        self._length = self._length + 1;
        if(self.empty()):
            self._head.set_prox(novo);
            novo.set_ant(self._head);
            novo.set_prox(self._syrup);
            self._syrup.set_ant(novo);
        else:
            aux = self._syrup.get_ant();
            aux.set_prox(novo);
            novo.set_ant(aux);
            novo.set_prox(self._syrup);
            self._syrup.set_ant(novo);

    def pop(self):
        self._length = self._length - 1;
        aux = self._syrup.get_ant();
        aux2 = aux.get_ant();
        aux2.set_prox(self._syrup);
        self._syrup.set_ant(aux2);
        del aux;

    def last(self):
        return self._head.get_prox();

    def top(self):
        return self._syrup.get_ant();

    def printSt(self):
        aux = self._syrup.get_ant();
        while(aux != self._head):
            print(aux.get_value(), " ");
            aux = aux.get_ant();
