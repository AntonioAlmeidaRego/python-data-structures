from NodeTree import NodeTree
from SearchUtil import SearchUtil
from stack.Stack import Stack


class TreeBinary:
    def __init__(self, value):
        self._root = NodeTree()
        self._size = 0
        self._nodeAux = NodeTree()
        self._size = self._size + 1
        self._root.__set_value__(value)
        self._stack = Stack()
        self._stack.__push__(value, 0)

    def _is_child_left(self, root):
        if (root.__get_left__() != None):
            return True
        return False

    def _is_child_right(self, root):
        if (root.__get_right__() != None):
            return True
        return False

    def _child(self, root, value):
        if ((root.__get_value__() < value) and (self._is_child_left(root) == False)):
            return root

        if ((root.__get_value__() > value) and (self._is_child_right(root) == False)):
            return root

        if ((root.__get_value__() < value) and (root.__get_left__() != None)):
            return self._child(root.__get_left__(), value)

        if ((root.__get_value__() > value) and (root.__get_right__() != None)):
            return self._child(root.__get_right__(), value)

        return root

    def __is_empty_left(self):
        if (self._root.__get_left__() != None):
            return True
        return False

    def __is_empty_right(self):
        if (self._root.__get_right__() != None):
            return True
        return False

    def __root__(self):
        return self._root

    def __size__(self):
        return self._size

    def __insert__(self, value):
        self._size = self._size + 1
        self._stack.__push__(value, 0)
        if ((self.__is_empty_left() == False) and (value < self._root.__get_value__())):
            node = NodeTree()
            node.__set_father__(self._root)
            node.__set_value__(value)
            self._root.__set_left__(node)
        elif ((self.__is_empty_right() == False) and (value > self._root.__get_value__())):
            node = NodeTree()
            node.__set_value__(value)
            node.__set_father__(self._root)
            self._root.__set_right__(node)
        else:
            if (value < self._root.__get_value__()):
                child = self._child(self._root.__get_left__(), value)
                if (child != None):
                    if (value > child.__get_value__()):
                        node = NodeTree()
                        node.__set_value__(value)
                        node.__set_father__(child)
                        child.__set_right__(node)
                    else:
                        node = NodeTree()
                        node.__set_value__(value)
                        node.__set_father__(child)
                        child.__set_left__(node)

            else:
                child = self._child(self._root.__get_right__(), value)
                if (child != None):
                    if (value > child.__get_value__()):
                        node = NodeTree()
                        node.__set_value__(value)
                        node.__set_father__(child)
                        child.__set_right__(node)
                    else:
                        node = NodeTree()
                        node.__set_value__(value)
                        node.__set_father__(child)
                        child.__set_left__(node)

    def __search_node__(self, root, value):
        if (root == self._root):
            if (value > root.__get_value__()):
                root = root.__get_right__()
                self._nodeAux = root
            elif (value < root.__get_value__()):
                root = root.__get_left__()
                self._nodeAux = root
            else:
                return root

        if (value == self._nodeAux.__get_value__()):
            return self._nodeAux
        else:
            if ((root.__get_left__() != None) and (root.__get_value__() != value)):
                self._nodeAux = root.__get_left__()
                self.__search_node__(root.__get_left__(), value)
            if ((root.__get_right__() != None) and (root.__get_value__() != value)):
                self._nodeAux = root.__get_right__()
                self.__search_node__(root.__get_right__(), value)

        return self._nodeAux

    def __is_leaf__(self, root):
        if (root.__get_left__() == None and root.__get_right__() == None):
            return True
        return False

    def __search_min__(self, root, value):
        search = SearchUtil(self._stack.__extract_values__())

        if (root == self._root):
            node = self.__search_node__(root, value)
            if (self.__is_leaf__(node)):
                return None
            if (value > root.__get_value__()):
                root = root.__get_right__()
                self._nodeAux = root
            if (value < root.__get_value__()):
                root = root.__get_left__()
                self._nodeAux = root

        searchRet = search.search_for_previous_value(value)
        if (searchRet == self._nodeAux.__get_value__()):
            return self._nodeAux
        if (root.__get_left__() != None and searchRet != self._nodeAux.__get_value__()):
            self._nodeAux = root.__get_left__()
            self.__search_min__(root.__get_left__(), value)
        if (root.__get_right__() != None and searchRet != self._nodeAux.__get_value__()):
            self._nodeAux = root.__get_right__()
            self.__search_min__(root.__get_right__(), value)

        return self._nodeAux

    def __extract_values__(self):
        return self._stack.__extract_values__()

    def __remove__(self, root, value):
        self._size = self._size - 1
        nodeTree = self.__search_node__(root, value)
        if (nodeTree != None):
            nodeFather = nodeTree.__get_father__()
            if (nodeFather != None):
                self._stack.__pop_value__(value)
                if (self._is_child_left(nodeTree) and self._is_child_right(nodeTree)):
                    nodeMin = self.__search_min__(root, value)
                    nodeMin.__set_father__(nodeFather)
                    if (nodeTree.__get_value__() > nodeMin.__get_value()):
                        nodeMin.__set_right__(nodeTree.__get_right__())
                        nodeTree.__get_right__().__set_father(nodeMin)
                    else:
                        nodeTree.__get_left__().__set_father(nodeMin)
                        nodeMin.__set_left__(nodeTree.__get_left__())

                    if (nodeFather.__get_value__() > nodeMin.__get_value__()):
                        nodeFather.__set_left__(nodeMin)
                    else:
                        nodeFather.__set_right__(nodeMin)
                else:
                    if (self.__is_leaf__(nodeTree)):
                        if (nodeTree.__get_value__() < nodeFather.__get_value__()):
                            nodeFather.__set_left__(None)
                        else:
                            nodeFather.__set_right__(None)
                    else:
                        if (nodeTree.__get_value__() < nodeFather.__get_value__()):
                            if (not self._is_child_left(nodeTree) and self._is_child_right(nodeTree)):
                                nodeTree.__get_right__().__set_father__(nodeFather)
                                nodeFather.__set_left__(nodeTree.__get_right__())
                            else:
                                nodeTree.__get_left__().__set_father__(nodeFather)
                                nodeFather.__set_left__(nodeTree.__get_left__())
                        else:
                            if (not self._is_child_left(nodeTree) and self._is_child_right(nodeTree)):
                                nodeTree.__get_right__().__set_father__(nodeFather)
                                nodeFather.__set_right__(nodeTree.__get_right__())
                            else:
                                nodeTree.__get_right__().__set_father__(nodeFather)
                                nodeFather.__set_right__(nodeTree.__get_left__())

            else:
                if (nodeTree == self._root):
                    if (self._is_child_left(nodeTree) and self._is_child_right(nodeTree)):
                        nodeMin = self.__search_min__(self._root, value)
                        nodeFatherRemove = nodeMin.__get_father__()
                        if (nodeFatherRemove.__get_value__() > nodeMin.__get_value__()):
                            if (not self._is_child_left(nodeMin) and not self._is_child_right(nodeMin)):
                                nodeFatherRemove.__set_left__(None)
                            else:
                                if (self._is_child_left(nodeMin) and not self._is_child_right(nodeMin)):
                                    nodeFatherRemove.__set_left__(nodeMin.__get_left__())
                                else:
                                    if (not self._is_child_left(nodeMin) and self._is_child_right(nodeMin)):
                                        nodeFatherRemove.__set_left__(nodeMin.__get_right__())
                        else:
                            if (not self._is_child_left(nodeMin) and not self._is_child_right(nodeMin)):
                                nodeFatherRemove.__set_right__(None)
                            else:
                                if (self._is_child_left(nodeMin) and not self._is_child_right(nodeMin)):
                                    nodeFatherRemove.__set_right__(nodeMin.__get_left__())
                                else:
                                    if (not self._is_child_left(nodeMin) and self._is_child_right(nodeMin)):
                                        nodeFatherRemove.__set_right__(nodeMin.__get_right__())

                        nodeMin.__set_left__(self._root.__get_left__())
                        nodeMin.__set_right__(self._root.__get_right__())
                        nodeMin.__set_father__(None)
                        self._root = nodeMin
                    else:
                        if (not self._is_child_left(nodeTree) and not self._is_child_right(nodeTree)):
                            nodeTree = None
                            self._root = nodeTree
                        else:
                            if (self._is_child_left(nodeTree) and not self._is_child_right(nodeTree)):
                                child = nodeTree.__get_left__()
                                child.__set_left__(None)
                                child.__set_right__(None)
                                child.__set_father__(None)
                                self._root = child
                            else:
                                if (not self._is_child_left(nodeTree) and self._is_child_right(nodeTree)):
                                    child = nodeTree.__get_right__()
                                    child.__set_left__(None)
                                    child.__set_right__(None)
                                    child.__set_father__(None)
                                    self._root = child
