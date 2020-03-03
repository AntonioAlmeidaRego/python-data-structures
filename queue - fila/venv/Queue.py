from Node import Node

class Queue:

    def __init__(self):
        self._head = Node();
        self._syrup = Node();
        self._head.set_prox(self._syrup);
        self._head.set_ant(self._syrup);
        self._syrup.set_prox(self._head);
        self._syrup.set_ant(self._head);
        self._length = 0;

    def empty(self):
        if(self._head.get_prox() == self._syrup):
            return True;
        return False;

    def enqueue(self, value, key):
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

    def dequeue(self):
        self._length = self._length - 1;
        aux = self._head.get_prox();
        aux2 = aux.get_prox();
        self._head.set_prox(aux2);
        aux2.set_ant(self._head);
        del aux;

    def front(self):
        return self._head.get_prox();

    def back(self):
        return self._syrup.get_ant();

    def size(self):
        return self._length;

    def printQe(self):
        aux = self._head.get_prox();
        while (aux != self._syrup):
            print(aux.get_value());
            aux = aux.get_prox();
