#!/usr/bin/env python3
"""
A custom progress bar implementation for iterating over a list with ETA and progress display.
"""

import time
from typing import Iterable, Any


def ft_progress(lst: Iterable[Any]) -> Iterable[Any]:
    """
    A progress bar generator that yields elements from the list while displaying progress.

    Args:
        lst: The iterable to process.

    Yields:
        Elements from the input iterable.
    """
    start = time.time()
    total = len(lst)
    for i, elem in enumerate(lst):
        elapsed = time.time() - start
        rate = (i + 1) / elapsed if elapsed > 0 else 0
        eta = (total - (i + 1)) / rate if rate > 0 else 0
        percent = (i + 1) / total * 100

        bar_length = 50
        filled = int(percent / 2)
        bar = '=' * filled + '>' + ' ' * (bar_length - filled - 1) if filled < bar_length else '=' * bar_length

        print(f"\rETA: {eta:5.2f}s [{percent:6.2f}%][{bar}] {i+1}/{total} | elapsed time {elapsed:5.2f}s",
              end='', flush=True)
        yield elem
    print()


if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)