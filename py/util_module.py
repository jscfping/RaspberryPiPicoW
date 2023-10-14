

import time
import random
import io_module


def get_ms():
    return time.monotonic() * 1000


def sleep(ms):
    time.sleep(ms / 1000)


def getRandms(min, max):
    return random.randint(min, max)


def wait():
    while io_module.is_on():
        sleep(50)


def relax(min_ms, max_ms):
    sleep(getRandms(min_ms, max_ms))
