import dis

def incr_list(l):
    l[0] += 1

dis.dis(incr_list)


