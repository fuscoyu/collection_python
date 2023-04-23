# coding=utf-8

import heapq

class TopK:
    
    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable

    def push(self, val):
        if len(self.minheap) >= self.capacity:
            min_val = self.minheap[0]
            if val < min_val:
                pass
            else:
                heapq.heapreplace(self.minheap, val)
        else:
            heapq.heappush(self.minheap, val)

    def get_topk(self):
        for val in self.iterable:
             self.push(val)
        return self.minheap

if __name__ == '__main__':
     
    import random
    i = list(range(1000))
    random.shuffle(i)
    _ = TopK(i, 10)
    print _.get_topk()
    
