def flist(l):
    l.append(0)
    print(l)

l = []
flist(l)
flist(l)
print(l)

def fstr(s):
    print(id(s))
    s += 'a'
    print(id(s))
    print(s)
s = 'hehe'
fstr(s)
fstr(s)


def clear_list(l):
    print(id(l))
    l = []
    print(id(l))

ll = [1,2,3]
clear_list(ll)
print(ll)




def flist(l=[1]):
    print(id(l))
    l.append(1)
    print(l)


flist()
flist()
