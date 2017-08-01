import random
import time


def random_sleep():
    random_sleep_time = random.randint(50, 100) / 100
    time.sleep(random_sleep_time)