def coro():
    hello = yield 'hello'
    yield hello

c = coro()
print(next(c))

print(c.send('world'))


