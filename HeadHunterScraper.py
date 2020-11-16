import urllib.parse
import requests
from bs4 import BeautifulSoup


from parsing_functions import *


class HeadHunterScraper:

    def __init__(self):
        self.__default_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/72.0.3626.119 Safari/537.36'
        }
        self.__base = 'https://{0}.hh.kz/search/vacancy?{1}'
        self.__default_params = {
            'search_field': '',
            # Almaty 160
            'area': 160,
            'salary': '',
            'currency_code': 'KZT',
            'experience': 'doesNotMatter',
            'order_by': 'relevance',
            'search_period': '1',
            'items_on_page': 100,
            'no_magic': 'true',
            # 'from': 'suggest_post',
            'specialization': 1
        }
        self.vacancies_count = 0

    def merge_params(fn):
        def wrapper(self, city, **kwargs):
            merged_params = dict(self.__default_params)
            merged_params.update(kwargs)
            return fn(self, city, **merged_params)

        return wrapper

    @merge_params
    def parse(self, city, **kwargs):
        page = 0
        is_next = True
        json_dict = {}
        url = self.__url_resolver(city, **kwargs)
        print(url)

        while is_next:
            html = self.__get_page(url, page)
            soup = BeautifulSoup(html, "html.parser")
            raw_vacancies = soup.findAll('div', attrs={'class': "vacancy-serp-item"})
            is_next = soup.find('a', attrs={'data-qa': "pager-next"}) is not None
            for vacancy in raw_vacancies:
                min_array = {
                    "vacancy_city": str.split(get_city(vacancy), ',')[0],
                    "vacancy_name": get_vacancy_title(vacancy),
                    "vacancy_zp": get_vacancy_zp(vacancy),
                    "vacancy_link": get_vacancy_link(vacancy),
                    "vacancy_desc": get_vacancy_desc(vacancy),
                    "vacancy_requirement": get_vacancy_requirement(vacancy),
                    "company_name": get_vacancy_company_name(vacancy),
                    "date_of_post": get_date_of_post_vacancy(vacancy)
                }
                self.vacancies_count += 1
                print(self.vacancies_count)
                json_dict[get_vacancy_id(vacancy)] = min_array

            page += 1
        return json_dict

    def get_count_of_vacancies(self):
        return self.vacancies_count

    def __url_resolver(self, city, **params):
        query = urllib.parse.urlencode(params)
        return self.__base.format(city, query)

    def __get_page(self, url, number):
        return self.__get_html(url + '&page=' + str(number))

    def __get_html(self, url):
        req = requests.get(url, headers=self.__default_headers)
        return req.content
