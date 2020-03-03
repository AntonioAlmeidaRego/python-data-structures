from Node import Node

class Queue:

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

    def enqueue(self, value, key):
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

    def dequeue(self):
        aux = self.head.get_prox();
        aux2 = aux.get_prox();
        self.head.set_prox(aux2);
        aux2.set_ant(self.head);
        del aux;

    def printQe(self):
        aux = self.head.get_prox();
        while(aux != self.syrup):
            print(aux.get_value(), " ");
            aux = aux.get_prox(); 