#!/home/minquan/.conda/envs/ai-lab/bin/python
import re
from document_parser import get_soup
import requests
import time
import random
from fifo_q import Queue as Q
import csv


def get_movie_info(soup):
    rating = soup.find('strong', {'class': 'll rating_num'}).text

    movie_name = soup.find('span', {'property': "v:itemreviewed"}).text
    year = soup.find('span', {'class': 'year'}).text

    movie_info = {
        'rating': rating,
        'name': movie_name,
        'year': year.replace('(', '').replace(')', '')
    }

    return movie_info


def get_recommends_list(soup):
    recommends = soup.find('div', {'class': 'recommendations-bd'})
    names = [a['alt'] for a in recommends.find_all('img')]
    ids = [re.search('subject/(.*)/', a['href']).group(1)
             for ii, a in enumerate(recommends.find_all('a'))
             if ii % 2 == 0]

    return list(zip(names, ids))


def get_subject_page_by_movie_id(movie_id):
    return "https://movie.douban.com/subject/{}/".format(movie_id)


def extract_movie_info(f):
    def _extract(movie_id):
        url = get_subject_page_by_movie_id(movie_id)
        r = requests.get(url)
        if r.status_code == 200: return f(get_soup(r.text))
        else: raise LookupError
    return _extract


get_movie_recommendation = extract_movie_info(get_recommends_list)
get_movie_abstract = extract_movie_info(get_movie_info)


def add_ids_to_queue(queue, recommendations):
    [queue.push(ID) for name, ID in recommendations]
    return queue


def movie_info_saver(info_file):
    csvfile = open(info_file, 'w', newline='')
    spamwrite = csv.writer(csvfile)
    spamwrite.writerow(['id', 'douban_id', 'name', 'year', 'rating'])

    def _save(number, movie_id):
        movie_info = get_movie_abstract(movie_id)
        print("{}: {}".format(number, movie_info))
        spamwrite.writerow([
            number, movie_id, movie_info['name'], movie_info['year'], movie_info['rating']
        ])

    return _save


def get_recommendation_by_bfs(movie_id):

    visted = set()

    max_length = 100000
    queue = Q(length=max_length)

    for _id in movie_id: queue.push(_id)

    number = 0

    save_info = movie_info_saver('movie_info.csv')

    while 0 < len(queue) < max_length:
        movie_id = queue.pop()

        if movie_id in visted: continue
        else: visted.add(movie_id)

        try:
            recommendations = get_movie_recommendation(movie_id)
            save_info(number, movie_id)
        except LookupError as e:
            print('error connection')
            break

        queue = add_ids_to_queue(queue, recommendations)

        print(movie_id)

        number += 1

        random_sleep_time = random.randint(50, 100) / 100
        time.sleep(random_sleep_time)

    for ID in queue:
        try: save_info(number, ID)
        except LookupError as e: break
        number += 1

    return number


if __name__ == '__main__':
    # movie_info = get_movie_info(get_soup(get_html_doc('movie_subject.html')))
    # recommends = get_recommends_list(get_soup(get_html_doc('movie_subject.html')))
    # print(movie_info)
    # print(recommends)

    ids = ['26363254', '1849031', '26289138', '2567647']

    movies = get_recommendation_by_bfs(ids)
