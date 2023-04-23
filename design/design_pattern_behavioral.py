# coding=utf-8

# 发布订阅模式 观察者模式

class Pubilsher:

    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}').format(observer)

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}').format(observer)

    def notify(self):
        [o.notify_by(self) for o in self.observers]

class Formatter(Pubilsher):

    def __init__(self, name):
        self.name = name
 
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        self._data = int(new_value)
        self.notify()

class BinaryFormatter:

    def notify_by(self, publisher):
        print("{}:'{}' has now bin data = {}".format(
                 type(self).__name__, pushlisher.name, bin(publisher.data)))


df = Formatter('formatter')
bf = BinaryFormatter()
df.add(bf)
df.data = 3

