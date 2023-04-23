# coding=utf-8

from collections import deque

class Stack:
    def __init__(self):
        self.items = deque() # 或用list

    def push(self, val):
        return self.items.append(val)
    
    def pop(self):
        return self.items.pop()

    def __iter__(self):
        res = []
        for i in self.items:
            res.append(i)
 
        for i in reversed(res):
            yield i

def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(dir(s))
    for i in s:
        print(i)
test_stack()

