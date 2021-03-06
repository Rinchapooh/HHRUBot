"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/72.0.3626.119 Safari/537.36'
}

url = "https://almaty.hh.kz/search/vacancy?clusters=true&enable_snippets=true&items_on_page=25&no_magic=true&showClusters=true"

req = requests.get(url, headers=headers)
html = req.content

soup = BeautifulSoup(html, "html.parser")
raw_vacancies = soup.findAll('div', attrs={'class': "vacancy-serp-item"})
"""


def get_date_of_post_vacancy(vac):
    return vac.find('span', attrs={'data-qa': "vacancy-serp__vacancy-date"}).text.replace("&nbsp;", "")


def get_vacancy_company_name(vac):
    try:
        company_name = vac.find('a', attrs={'data-qa': "vacancy-serp__vacancy-employer"}).text
        return company_name
    except:
        pass


def get_vacancy_requirement(vac):
    return vac.find('div', attrs={'data-qa': "vacancy-serp__vacancy_snippet_requirement"}).text


def get_vacancy_desc(vac):
    return vac.find('div', attrs={'data-qa': "vacancy-serp__vacancy_snippet_responsibility"}).text


def get_vacancy_link(vac):
    return vac.find('a', attrs={'data-qa': "vacancy-serp__vacancy-title"}).get('href')


def get_city(vac):
    return vac.find('span', attrs={'data-qa': "vacancy-serp__vacancy-address"}).text


def get_vacancy_title(vac):
    return vac.find('a', attrs={'data-qa': "vacancy-serp__vacancy-title"}).text


def get_vacancy_id(vac):
    string_id = vac.find('a', attrs={'data-qa': "vacancy-serp__vacancy-title"}).get('href')
    return str.split(string_id, "/", -1)[-1]


def get_employer_logo_id(vac):
    try:
        employer_logo_id = vac.find('a', attrs={'data-qa': "vacancy-serp__vacancy-employer-logo"}).get('href')
        return str.split(employer_logo_id, '/', 2)[-1]
    except:
        pass


def get_vacancy_zp(vac):
    try:
        zp = vac.find('span', attrs={'data-qa': "vacancy-serp__vacancy-compensation"}).text
        return zp
    except:
        return


def get_employer_id(vac):
    try:
        employer_id = vac.find('a', attrs={'data-qa': "vacancy-serp__vacancy-employer"}).get('href')
        return str.split(employer_id, '/', 2)[-1]
    except:
        print('***NO_EMPLOYER_ID***')
        return
