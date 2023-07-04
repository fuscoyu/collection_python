from collections import OrderedDcit


class LRUCache:
    def __init__(self, capacity=128):
        self.od = OrderedDcit()
        self.capacity = capacity

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)
