
from Node import Node


class Stack:
    def __init__(self):
        self.head = Node();
        self.syrup = Node();
        self.head.set_prox(self.syrup);
        self.head.set_ant(self.syrup);
        self.syrup.set_prox(self.head);
        self.syrup.set_ant(self.head);

    def empty(self):
        if(self.head.get_prox() == self.syrup):
            return True;
        return False;

    def push(self, value, key):
        novo = Node();
        novo.set_key(key);
        novo.set_value(value);
        if(self.empty()):
            self.head.set_prox(novo);
            novo.set_ant(self.head);
            novo.set_prox(self.syrup);
            self.syrup.set_ant(novo);
        else:
            aux = self.syrup.get_ant();
            aux.set_prox(novo);
            novo.set_ant(aux);
            novo.set_prox(self.syrup);
            self.syrup.set_ant(novo);

    def pop(self):
        aux = self.syrup.get_ant();
        aux2 = aux.get_ant();
        aux2.set_prox(self.syrup);
        self.syrup.set_ant(aux2);
        del aux;

    def printSt(self):
        aux = self.head.get_prox();
        while(aux != self.syrup):
            print(aux.get_value(), " ");
            aux = aux.get_prox();
