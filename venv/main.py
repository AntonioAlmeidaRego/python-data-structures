from TreeBinary import TreeBinary
from SearchUtil import SearchUtil
from stack.Stack import Stack
from deque.Deque import Deque
from queue.Queue import Queue

print ("#------ Deque -----#")
deque = Deque()
deque.__push_front__(25, 0)
deque.__push_front__(35, 1)
deque.__push_front__(15, 2)
deque.__push_back__(75, 3)
deque.__push_back__(39, 4)
deque.printDq()
print ("#------------------#")
print ("#------ Queue -----#")

queue = Queue()
queue.__enqueue__(25, 0)
queue.__enqueue__(35, 1)
queue.__enqueue__(15, 2)
queue.__enqueue__(75, 3)
queue.__enqueue__(39, 4)
queue.__printQe__()
print ("#------------------#")
print ("#------ Stack -----#")

stack = Stack()
stack.__push__(25, 0)
stack.__push__(35, 1)
stack.__push__(15, 2)
stack.__push__(75, 3)
stack.__push__(39, 4)
stack.__printSt__()
print ("#------------------#")
print ("#----- Tree Binary ----#")
tree = TreeBinary(25)
tree.__insert__(12)
tree.__insert__(35)
tree.__insert__(45)
tree.__insert__(5)
tree.__pre_ordem__(tree.__root__())


