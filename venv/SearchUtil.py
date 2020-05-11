class SearchUtil:
    def __init__(self, array):
        self._array = array


    def __sort_by_biggest(self):
        for i in range(0, len(self._array)):
            for j in range(i+1, len(self._array)):
                if(self._array[i] < self._array[j]):
                    aux = self._array[i]
                    self._array[i] = self._array[j]
                    self._array[j] = aux

    def __sort_by_smallest(self):
        for i in range(0, len(self._array)):
            for j in range(i+1, len(self._array)):
                if(self._array[i] > self._array[j]):
                    aux = self._array[i]
                    self._array[i] = self._array[j]
                    self._array[j] = aux

    def __loop_fim(self, loop):
        if(loop == len(self._array)):
            return True
        return False

    def __search_for_next_value__(self, value):
        self.__sort_by_biggest()
        loop = 0
        while(True):
            element = self._array[loop]
            if(element == value):
                return self._array[loop-1]
            else:
                if(value > element):
                    if(loop > 0):
                        loop = loop -1
                    break

                if(value < element):
                    loop = loop + 1

                if(self.__loop_fim(loop)):
                    loop = loop + 1
                    break

        return self._array[loop]

    def search_for_previous_value(self, value):
        self.__sort_by_smallest()
        loop = 0
        while (True):
            element = self._array[loop]
            if (element == value):
                return self._array[loop - 1]
            else:
                if (value > element):

                    loop = loop + 1

                if (value < element):
                    if (loop > 0):
                        loop = loop - 1
                    break

                if (self.__loop_fim(loop)):
                    loop = loop - 1
                    break

        return self._array[loop]