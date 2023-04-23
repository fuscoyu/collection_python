from functools import wraps

def cache(func):
    store = {}

    @wraps(func):
    def _(n):
        if n in store:
            return store[n]
        else:
            res = func(n)
            store[n] = res
            return res
        return _


@cache
def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-2)


