import argparse
import Core.jsons

from Core import HeadHunterScraper

arg_parser = argparse.ArgumentParser(description="Collection of vacancies from the site hh.ru.")

arg_parser.add_argument('-a', '--area', dest='area', default='almaty')
arg_parser.add_argument('-s', '--spec', dest='specialization', default='it')
arg_parser.add_argument('-p', '--period', dest='search_period', default='1')
arg_parser.add_argument('-i', '--items', dest='items_on_page', default='50')
# parser.add_argument('-t', '--t', dest='text', default='python')
# parser.add_argument('-c', dest='city', default='almaty')
# parser.add_argument('-s', dest='search_files', default='name')
# parser.add_argument('-e', dest='experience', default='doesNotMatter')
# parser.add_argument('-f', dest='filename', default='output' required=True)
# parser.add_argument('--exporter', default='csv')

args = arg_parser.parse_args()

scraper = HeadHunterScraper.HeadHunterScraper()


# args_lib = {
#     "spec": {"buh": 2, "it": 1, "gov": 16, "sales": 17},
#     "area": {"astana": 159, "almaty": 160, "kz": 40},
# }


def get_code(common_code):
    if str.lower(common_code) == 'it':
        return '1'
    elif str.lower(common_code) == 'buh':
        return '2'
    elif str.lower(common_code) == 'sales':
        return '17'
    elif str.lower(common_code) == 'almaty':
        return '160'
    elif str.lower(common_code) == 'astana':
        return '159'
    elif str.lower(common_code) == 'kz':
        return '40'
    else:
        exit("[*]=====Error paring arguments===")


def parse(specialization_code, area_code, items_on_page, period):
    parsed = scraper.parse("almaty",
                           specialization=specialization_code,
                           area=area_code,
                           items_on_page=items_on_page,
                           search_period=period)

    Core.jsons.write_json_to_disk(parsed,
                                  va_count=scraper.vacancies_count,
                                  va_specialization=specialization_code,
                                  va_area=area_code)


parse(get_code(args.specialization), get_code(args.area), args.items_on_page, args.search_period)
