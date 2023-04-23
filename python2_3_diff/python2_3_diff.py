#!/bin/env/python
# coding=utf-8

class Base(object):
    def hello(self):
        print('hello')


class C(Base):
    def hello(self):
        #py2
        return super(C, self).hello()


c = C()
c.hello()

class C2(Base):
    def hello(self):
        #py3
        return super().hello()


c2 = C2()
c2.hello()
