import argparse
import Core.jsons

from Core import HeadHunterScraper

arg_parser = argparse.ArgumentParser(description="Collection of vacancies from the site hh.ru.")

arg_parser.add_argument('-a', '--area', dest='area', default='almaty')
arg_parser.add_argument('-s', '--spec', dest='specialization', default='it')
arg_parser.add_argument('-p', '--period', dest='search_period', default='1')
arg_parser.add_argument('-i', '--items', dest='items_on_page', default='50')
arg_parser.add_argument('-t', '--t', dest='text', default='')
# parser.add_argument('-c', dest='city', default='almaty')
# parser.add_argument('-s', dest='search_files', default='name')
# parser.add_argument('-e', dest='experience', default='doesNotMatter')
# parser.add_argument('-f', dest='filename', default='output' required=True)
# parser.add_argument('--exporter', default='csv')

args = arg_parser.parse_args()

scraper = HeadHunterScraper.HeadHunterScraper()

names_codes = \
    {
        'specs': {'it': '1', 'buh': '2', 'sales': '17'},
        'areas': {'astana': '159', 'almaty': '160', 'kz': '40', 'shymkent': '205'},
        'periods': {'day': '1', 'week': '7', 'month': '30'}
    }


# def get_code(common_code):
#     if str.lower(common_code) == 'it':
#         return '1'
#     elif str.lower(common_code) == 'buh':
#         return '2'
#     elif str.lower(common_code) == 'sales':
#         return '17'
#     elif str.lower(common_code) == 'almaty':
#         return '160'
#     elif str.lower(common_code) == 'astana':
#         return '159'
#    # elif str.lower(common_code) == 'shymkent' or 'shym':
#       #  return '205'
#     elif str.lower(common_code) == 'kz':
#         return '40'
#     elif str.lower(common_code) == 'day' or '1day':
#         return '1'
#     elif str.lower(common_code) == 'week' or '7days':
#         return '7'
#     elif str.lower(common_code) == 'month' or 'mont':
#         return '30'
#
#     else:
#         exit("[*]=====Error paring arguments==="
#              "\nExample: console.py -s sales -a almaty -p 7days")


def parse(specialization_code, area_code, period, text):

    parsed = scraper.parse("almaty",
                           specialization=specialization_code,
                           area=area_code,
                           search_period=period,
                           text=text)

    Core.jsons.write_json_to_disk(parsed,
                                  va_count=scraper.vacancies_count,
                                  va_specialization=specialization_code,
                                  va_area=area_code)


parse(names_codes['specs'].get(args.specialization),
      names_codes['areas'].get(args.area),
      names_codes['periods'].get(args.search_period),
      text=args.text)
