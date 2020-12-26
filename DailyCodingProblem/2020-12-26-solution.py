import time


def scheduler(f, n):
    time.sleep(n/1000)
    f()
