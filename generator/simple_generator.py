def simple_generator():
    yield 'hello'
    yield 'world'


gen = simple_generator()

print(type(gen))
print(next(gen))
print(next(gen))
