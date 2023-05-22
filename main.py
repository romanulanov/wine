import argparse
import datetime
import os
import pandas
import collections
from argparse import RawTextHelpFormatter
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


COMPANY_FOUNDATION_YEAR = 1920 


def clarify_age(age):
    if (age % 10 == 1) and (age != 11) and (age != 111):
        return f'{str(age)}{" год"}' 
    elif (age % 10 > 1) and (age % 10 < 5) and (age != 12) and (age != 13) and (age != 14):
        return f'{str(age)}{" года"}'
    else:
        return f'{str(age)}{" лет"})'


def main():
    parser = argparse.ArgumentParser(description='Магазин элитного вина.\nЗапустить сайт с готовой таблицей можно с помошью команды:\npython3 main.py\nЧтобы сайт взял данные с вашей таблицы, укажите путь с именем таблицы после команды: \npython3 main.py my_wine.xlsx  ', formatter_class=RawTextHelpFormatter)
    parser.add_argument ('path_table', nargs='?', default='wine.xlsx')
    args = parser.parse_args()
    path_table = args.path_table

    excel_data = (pandas.read_excel(path_table, sheet_name='Лист1', na_values=['N/A', 'NA'], keep_default_na=False)).to_dict(orient='records')
    wines = collections.defaultdict(list)
    for wine in excel_data:
        wines[wine['Категория']] += [wine]
    wines = dict(sorted(wines.items()))
    age = datetime.datetime.now().year-COMPANY_FOUNDATION_YEAR 

    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    rendered_page = template.render(wines=wines, age=clarify_age(age))
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
