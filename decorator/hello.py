# ecoding:utf8

"""
装饰器 函数式编程
"""


def hello(fn):
    def wrapper():
        print("hello, %s" % fn.__name__[::-1].upper())
        fn()
        print("goodby, %s" % fn.__name__)

    return wrapper


@hello
def foo():
    print("i am foo")


foo()
