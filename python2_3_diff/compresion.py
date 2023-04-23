a = ['a', 'b', 'c']

b = [1, 2, 3]

d = {}

for i in range(len(a)):
    d[a[i]] = b[i]
print(d)

e = {k:v for k, v in zip(a,b)}
print(e)
