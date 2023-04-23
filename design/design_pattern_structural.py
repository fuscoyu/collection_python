# coding=utf-8

# 适配器模式

class Dog(object):

    def __init__(self):
        self.name = 'Dog'

    def bark(self):
        return 'woof!'


class Cat(object):

    def __init__(self):
        self.name = 'Cat'

    def meow(self):
        return 'meow!'


class Adapter(object):

    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

objects = []

dog = Dog()
objects.append(Adapter(dog, make_noise=dog.bark))

cat = Cat()
objects.append(Adapter(cat, make_noise=cat.meow))

for obj in objects:
    print('A {0} goes {1}'.format(obj.name, obj.make_noise()))


