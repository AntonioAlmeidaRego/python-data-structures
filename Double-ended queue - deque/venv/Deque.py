from Node import Node

class Deque:

    def __init__(self):
        self._head = Node();
        self._syrup = Node();
        self._head.set_prox(self._syrup);
        self._head.set_ant(self._syrup);
        self._syrup.set_prox(self._head);
        self._syrup.set_ant(self._head);
        self.length = 0;

    def empty(self):
        if(self._head.get_prox() == self._syrup):
            return True;
        return False;

    def push_back(self, value, key):
        novo = Node();
        novo.set_value(value);
        novo.set_key(key);
        self.length = self.length + 1;
        if(self.empty()):
            self._head.set_prox(novo);
            novo.set_ant(self._head);
            novo.set_prox(self._syrup);
            self._syrup.set_ant(novo);
        else:
            aux = self._syrup.get_ant();
            novo.set_prox(self._syrup);
            novo.set_ant(aux);
            aux.set_prox(novo);
            self._syrup.set_ant(novo);

    def push_front(self, value, key):
        novo = Node();
        novo.set_value(value);
        novo.set_key(key);
        self.length = self.length + 1;
        if (self.empty()):
            self._head.set_prox(novo);
            novo.set_ant(self._head);
            novo.set_prox(self._syrup);
            self._syrup.set_ant(novo);
        else:
            aux = self._head.get_prox();
            novo.set_ant(self._head);
            novo.set_prox(aux);
            aux.set_ant(novo);
            self._head.set_prox(novo);

    def pop_back(self):
        self.length = self.length - 1;
        aux = self._syrup.get_ant();
        aux2 = aux.get_ant();
        aux2.set_prox(self._syrup);
        self._syrup.set_ant(aux2);
        del aux;

    def pop_front(self):
        self.length = self.length - 1;
        aux = self._head.get_prox();
        aux2 = aux.get_prox();
        aux2.set_ant(self._head);
        self._head.set_prox(aux2);
        del aux;

    def size(self):
        return self.length;

    def back(self):
        return self._syrup.get_ant();

    def front(self):
        return self._head.get_prox();

    def printDq(self):
        aux = self._head.get_prox(); 
        while(aux != self._syrup):
            print(aux.get_value());
            aux = aux.get_prox();