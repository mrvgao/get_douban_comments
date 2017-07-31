import requests
from document_parser import get_douban_comment_from_html


def get_one_page_comments(movie_id):
    page_num = 100
    base_url = "https://movie.douban.com/subject/{}/comments".format(movie_id)
    for i in range(page_num):
        start = "?start={}".format(i*20)
        url = base_url + start
        r = requests.get(url)

        if r.status_code == 200:
            yield r.text
        else:
            print(url)
            raise StopIteration


for page_comments in get_one_page_comments('26266085'):
    try:
        comments = get_douban_comment_from_html(page_comments)
        print(comments)
    except Exception:
        continue
