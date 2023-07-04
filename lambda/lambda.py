# /usr/bin/python3
import math

# anonymous function
# lambda argument_list:expersion

def sq(x):
    return x * x

def is_sqr(x):
    return math.sqrt(x) % 1 == 0

def main():
    # ret = map(sq, [y for y in range(10)])
    # print(list(ret))
    #
    # ret = map(lambda x: x * x, [y for y in range(10)])
    # print(list(ret))

    ret = filter(is_sqr, [y for y in range(10)])
    print(list(ret))

    ret = filter(lambda x: math.sqrt(x) % 1 == 0, [y for y in range(10)])
    print(list(ret))


main()
