# coding=utf-8
import shutil

def mycopy(source, dest):
    try:
        shutil.copy2(source, dest)
    except OSError: # python2 里丢失原来的traceback信息
        raise NotImplementedError("automatic sudo injection") from OSError


mycopy('old', 'new')
