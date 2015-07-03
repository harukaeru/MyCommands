import time
def time_deco(func):
    def _deco(*args, **kwargs):
        s = time.time()
        for x in range(1000):
            func(*args, **kwargs)
        e = time.time()
        print(e - s)
    return _deco
