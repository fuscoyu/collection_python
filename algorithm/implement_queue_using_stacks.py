# coding=utf-8

from collections import deque


class Stack(object):
    def __init__(self):
       self.items = deque()

    def push(self, x):
        return self.items.append(x)
    
    def pop(self):
        return self.items.pop()

    def top(self):
        print('-'*100)
        print(self.items)
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0



class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        return self.s1.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.s2.empty():
            return self.s2.pop()
        
        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.s2.empty():
            return self.s2.top()

        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)

        return self.s2.top() 

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.s1.empty() and self.s2.empty()

def test():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)

    print(q.pop())
    print(q.pop())
    print(q.pop())

test()
