# coding=utf-8

import threading
import time


def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1
    return True


def main1():
    thread_ary = {}
    start_time = time.time()
    for tid in range(2):
        t = threading.Thread(target=my_counter)
        t.start()
        t.join()

    print("单线程顺序执行total_time: {}".format(time.time() - start_time))


def main2():
    thread_ary = {}
    start_time = time.time()
    for tid in range(2):
        t = threading.Thread(target=my_counter)
        t.start()
        thread_ary[tid] = t
    for i in range(2):
        thread_ary[i].join()
    print("并发执行total_time: {}".format(time.time() - start_time))


if __name__ == "__main__":
    main1()
    main2()
