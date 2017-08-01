import re
from document_parser import get_soup
from document_parser import get_html_doc
import requests


def get_recommends_list(soup):
    recommends = soup.find('div', {'class': 'recommendations-bd'})
    names = [a['alt'] for a in recommends.find_all('img')]
    hrefs = [re.search('subject/(.*)/', a['href']).group(1) for a in recommends.find_all('a')]

    return list(zip(names, hrefs))


def get_subject_page_by_movie_id(movie_id):
    return "https://movie.douban.com/subject/{}/".format(movie_id)


def get_recommendation(movie_id):
    url = get_subject_page_by_movie_id(movie_id)
    r = requests.get(url).text
    recommends = get_recommends_list(get_soup(r))

    return recommends


if __name__ == '__main__':
    recommends = get_recommendation('1849031')
    print(recommends)
