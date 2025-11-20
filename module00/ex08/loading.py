from tqdm import *
from time import sleep

import time

def ft_progress(lst):
    start = time.time()
    total = len(lst)
    for i, elem in enumerate(lst):
        elapsed = time.time() - start
        rate = (i + 1) / elapsed if elapsed > 0 else 0
        eta = (total - (i + 1)) / rate if rate > 0 else 0
        percent = (i + 1) / total * 100

        bar = ('=' * int(percent // 2)).ljust(50)
        print(f"\rETA: {eta:5.2f}s [{percent:6.2f}%][{bar}] {i+1}/{total} | elapsed time {elapsed:5.2f}s",
              end='')
        yield elem
    print()


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
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