from tqdm import *
from time import sleep

import time

def progress(lst):
    start = time.time()
    total = len(lst)
    for  elem in lst:
        elapsed = time.time() - start
        rate = (elem + 1) / elapsed if elapsed > 0 else 0
        eta = (total - (elem + 1)) / rate if rate > 0 else 0
        percent = (elem + 1) / total * 100

        bar = (('=' * int(percent // 5) + '>') if int(percent // 5) < 20 else ('=' * 20)).ljust(20)
        print(f"\rETA: {eta:5.2f}s [{percent:6.2f}%][{bar}] {elem+1}/{total} | elapsed time {elapsed:5.2f}s",
              end='')
        yield elem
    print()


listy = range(1000)
ret = 0
for elem in progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)

# for char in ft_progress(['a','b','c','d']):
#     sleep(0.25)


# pbar = tqdm(total=100)
# for i in range(10):
#     sleep(0.1)
#     pbar.update(10)
# pbar.close()