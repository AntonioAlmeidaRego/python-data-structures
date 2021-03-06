from Node import Node


class Queue:

    def __init__(self):
        self._head = Node()
        self._syrup = Node()
        self._head.__set_prox__(self._syrup)
        self._head.__set_ant__(self._syrup)
        self._syrup.__set_prox__(self._head)
        self._syrup.__set_ant__(self._head)
        self._length = 0

    def __empty__(self):
        if (self._head.__get_prox__() == self._syrup):
            return True
        return False

    def __enqueue__(self, value, key):
        novo = Node()
        novo.__set_key__(key)
        novo.__set_value__(value)
        self._length = self._length + 1
        if (self.__empty__()):
            self._head.__set_prox__(novo)
            novo.__set_ant__(self._head)
            novo.__set_prox__(self._syrup)
            self._syrup.__set_ant__(novo)
        else:
            aux = self._syrup.__get_ant__()
            aux.__set_prox__(novo)
            novo.__set_ant__(aux)
            novo.__set_prox__(self._syrup)
            self._syrup.__set_ant__(novo)

    def __dequeue__(self):
        self._length = self._length - 1
        aux = self._head.__get_prox__()
        aux2 = aux.__get_prox__()
        self._head.__set_prox__(aux2)
        aux2.__set_ant__(self._head)
        del aux

    def __dequeue_key__(self, key):
        node = self.__get_key__(key)
        if (node != None):
            nodeAnt = node.__get_ant__()
            nodeProx = node.__get_prox__()

            nodeAnt.__set_prox__(nodeProx)
            nodeProx.__set_ant__(nodeAnt)
            self._length = self._length - 1
            del node

    def __dequeue_value__(self, value):
        node = self.__search__(value)
        if (node != None):
            nodeAnt = node.__get_ant__()
            nodeProx = node.__get_prox__()

            nodeAnt.__set_prox__(nodeProx)
            nodeProx.__set_ant__(nodeAnt)
            self._length = self._length - 1
            del node

    def __dequeue_value_and_key__(self, value, key):
        node = self.__search__(value)
        if (node != None):
            if (node.__get_key__() == key):
                nodeAnt = node.__get_ant__()
                nodeProx = node.__get_prox__()

                nodeAnt.__set_prox__(nodeProx)
                nodeProx.__set_ant__(nodeAnt)
                self._length = self._length - 1
                del node

    def __enqueue_to_key__(self, key, new_value):
        node = self.__get_key__(key)
        if (node != None):
            node.__set_value__(new_value)

    def __enqueue_to_value__(self, value_prev, value_new):
        node = self.__search__(value_prev)
        if (node != None):
            node.__set_value__(value_new)

    def __front__(self):
        return self._head.__get_prox__()

    def __back__(self):
        return self._syrup.__get_ant__()

    def __size__(self):
        return self._length

    def __extract_values__(self):
        aux = self._head.__get_prox__()
        array = []
        while (aux != self._syrup):
            array.append(aux.__get_value__())
            aux = aux.__get_prox__()

        return array

    def __search__(self, value):
        node = self._head.__get_prox__()

        while (node != self._syrup):
            if (node.__get_value__() == value):
                return node
            node = node.__get_prox__()

        return None

    def __get_key__(self, key):
        node = self._head.__get_prox__()

        while (node != self._syrup):
            if (node.__get_key__() == key):
                return node
            node = node.__get_prox__()

        return None

    def __printQe__(self):
        aux = self._head.__get_prox__()
        string = ""
        while (aux != self._syrup):
            string = string + str(aux.__get_value__()) + " "
            aux = aux.__get_prox__()
        print(string)
