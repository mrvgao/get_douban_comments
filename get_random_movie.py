import random
import requests


def get_random_url(bit=7):
    num = ""
    for i in range(bit):
        num += str(random.randint(0, 9))
    url = get_url_base_movie_id(num)
    return url


def get_url_base_movie_id(movie_id):
    url = "https://movie.douban.com/subject/2{}/comments".format(movie_id)
    return url


def test_url_is_valid(url):
    r = requests.get(url)
    if r.status_code == 200: return True
    else: print(r.status_code); return False


def get_one_valid_url():
    url = get_random_url()
    while not test_url_is_valid(url): url = get_random_url()
    return url


def get_valid_url_one_by_one():
    for i in range(int(1e7)):
        movie_id = '{0:0>7}'.format(i)
        print(movie_id)
        url = get_url_base_movie_id(movie_id)
        if test_url_is_valid(url):
            yield movie_id
    raise StopIteration

if __name__ == '__main__':
    result = 'valid_movie_id.txt'

    with open(result, 'a') as f:
        for index, movie_id in enumerate(get_valid_url_one_by_one()):
            print(movie_id)
            print(index)
            f.write(movie_id + '\n')
