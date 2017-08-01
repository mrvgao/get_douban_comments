import random
import time
import os
import pandas as pd
import csv


def get_douban_id(douban_id_info_directory):
    files = os.listdir(douban_id_info_directory)

    for file in files:
        file_name = os.path.join(douban_id_info_directory, file)
        contents = pd.read_csv(file_name).iterrows()
        for c in contents:
            yield c[1].douban_id


def random_sleep():
    random_sleep_time = random.randint(80, 200) / 100
    time.sleep(random_sleep_time)


def csv_saver(file, columns):
    csvfile = open(file, 'a+', newline='')
    spamwrite = csv.writer(csvfile)
    spamwrite.writerow(columns)

    def _save(row):
        spamwrite.writerow(list(row))

    return _save


if __name__ == '__main__':
    for ii, id in enumerate(get_douban_id('movie_info')):
        print(id)
        if ii > 5: break
