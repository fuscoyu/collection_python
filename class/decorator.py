# coding=utf-8
import time


def log_time(func):
    
    def _log(*args, **kwargs):
        beg = time.time()
        res = func(*args, **kwargs)
        print('use time:{}'.format(time.time()-beg))
        return res
    return _log


@log_time
def mysleep(): # ***没加冒号
    time.sleep(1) # ***没写sleep多久
newsleep = log_time(mysleep)
newsleep()
#mysleep()
