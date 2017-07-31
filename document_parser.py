from bs4 import BeautifulSoup
import re


def get_html_doc(html_path):

    html_doc = ""

    lines = open(html_path, encoding='utf-8').readlines()

    for line in lines:
        html_doc += line

    return html_doc


def get_soup(html_doc):
    return BeautifulSoup(html_doc, 'html.parser')


def get_movie_info(soup):
    """
    :param html_doc:
    :return:  movie's name, link
    """
    movie_summary = soup.find(class_="movie-summary")

    movie_ = movie_summary.find(class_="movie-pic")
    movie_link = movie_.find('a')['href']
    movie_info = movie_.find('img')['title']

    return movie_link, movie_info


def get_comments(soup):
    comments = soup.find_all('div', {'class': 'comment'})
    return comments


def get_comment_contents(comments):
    return [(s, c) for s, c in [parse_one_comment(c) for c in comments] if s is not None]


def parse_one_comment(comment):
    star = comment.find('span', {'class': re.compile('^allstar')})['class'][0][-2]
    content = comment.find_all('p')[-1].text.strip()

    return star, content


def get_complete_info(movie_info, comments_content):
    movie_link, movie_name= movie_info
    return [(movie_link, movie_name, c, s) for s, c in comments_content]


def get_douban_comment_from_html(html_doc):
    html_soup = get_soup(html_doc)
    movie_info = get_movie_info(html_soup)

    pl = get_comments(html_soup)

    complete_info = get_complete_info(movie_info, get_comment_contents(pl))
    return complete_info


if __name__ == '__main__':
    comments = get_douban_comment_from_html(get_html_doc('douban_comment_example.html'))

    for c in comments:
        print(c)







