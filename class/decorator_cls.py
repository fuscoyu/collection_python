# coding=utf-8
import time

class LogTime:
    def __init__(self, use_int=False):
        self.use_int = use_int
 
    def __call__(self, func):
        def _log(*args, **kwargs):
            beg = time.time()
            res = func(*args, **kwargs)
            if self.use_int: # ***use_int 写成 use_init
                print('use time: {}'.format(int(time.time()-beg)))
            else:
                print('use time: {}'.format(time.time()-beg))
            return res
        return _log

@LogTime(use_int=True)
def mysleep():
    time.sleep(1)

mysleep()
