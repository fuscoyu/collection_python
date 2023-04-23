#!/bin/env/python
# coding=utf-8

# dock typing

class Duck:
    def quck(self):
        print("gua gua")

class Person:
    def quck(self):
        print("我是人类，我也会gua gua 的叫")

def in_the_forest(duck):
    duck.quck()

def game():
    tang = Duck()
    fusco = Person()
    in_the_forest(tang) 
    in_the_forest(fusco) 
    # 自省
    print(type(tang)) # python2输出为<type 'instance'>   python3为<class '__main__.Duck'>
    print(type(fusco))
    print(isinstance(tang, Duck))
    print(isinstance(fusco, Person))

game()
