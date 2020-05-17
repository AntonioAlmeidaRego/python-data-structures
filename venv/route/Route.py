class Route:
    def __init__(self):
        self._printPRE = ""
        self._printPOS = ""
        self._printSYM = ""

    def __print_pre(self):
        return self._printPRE

    def __print_pos(self):
        return self._printPOS

    def __print_sym(self):
        return self._printSYM

    def __visitor_pre(self, root):
        self._printPRE = self._printPRE + str(root.__get_value__()) + " "

    def __visitor_pos(self, root):
        self._printPOS = self._printPOS + str(root.__get_value__()) + " "

    def __visitor_sym(self, root):
        self._printSYM = self._printSYM + str(root.__get_value__()) + " "

    def __pos_order__(self, root):
        if(root != None):
            if (root.__get_left__() != None):
                self.__pos_order__(root.__get_left__())
            if (root.__get_right__() != None):
                self.__pos_order__(root.__get_right__())
            self.__visitor_pos(root)

    def __symmetrical_order__(self, root):
        if(root != None):
            if (root.__get_left__() != None):
                self.__symmetrical_order__(root.__get_left__())
            self.__visitor_sym(root)
            if (root.__get_right__() != None):
                self.__symmetrical_order__(root.__get_right__())

    def __pre_order__(self, root):
        if(root != None):
            self.__visitor_pre(root)
            if (root.__get_left__() != None):
                self.__pre_order__(root.__get_left__())
            if (root.__get_right__() != None):
                self.__pre_order__(root.__get_right__())
