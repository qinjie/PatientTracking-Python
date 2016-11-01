import os
import inspect


def current_method_name():
    return inspect.stack()[1][3]

def parent_method_name():
    return inspect.stack()[2][3]

def touch(fname, times=None):
    fhandle = open(fname, 'a')
    try:
        os.utime(fname, times)
    finally:
        fhandle.close()
