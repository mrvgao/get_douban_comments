import requests
from document_parser import get_douban_comment_from_html
from utils import random_sleep
from utils import get_douban_id
from utils import csv_saver

visited = set()


def get_page_comments(movie_id):
    page_num = 100
    base_url = "https://movie.douban.com/subject/{}/comments".format(movie_id)
    for i in range(page_num):
        random_sleep()

        start = "?start={}".format(i*20)
        url = base_url + start
        r = requests.get(url)
        if r.status_code == 200:
            yield r.text
        else:
            print(r.status_code)
            print(url)
            raise StopIteration


def get_movie_comments(movie_id):
    for ii, comment_page in enumerate(get_page_comments(movie_id)):
        try:
            comments = get_douban_comment_from_html(comment_page)
            for c in comments: yield c
        except Exception as e:
            print(e)
            continue


def main(movie_info_dir, test_mode=False):
    save = csv_saver('movie_comments.csv', ['id', 'link', 'name', 'comment', 'star'])
    _id = 0
    for ii, movie_id in enumerate(get_douban_id(movie_info_dir)):
        if test_mode and ii > 2: break
        if movie_id in visited: continue
        for c in get_movie_comments(movie_id):
            _id += 1
            save([_id] + list(c))
            if _id % 10 == 0: print("{}-{}: {}".format(ii, _id, c))
        visited.add(movie_id)

if __name__ == '__main__':
    main('movie_info', test_mode=False)
