import argparse
import datetime
import os
import pandas
import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


YEAR_COMPANY = 1920


def clarify_age(age):
    if (age % 10 == 1) and (age != 11) and (age != 111):
        return f'{str(age)}{" год"}' 
    elif (age % 10 > 1) and (age % 10 < 5) and (age != 12) and (age != 13) and (age != 14):
        return f'{str(age)}{" года"}'
    else:
        return f'{str(age)}{" лет"})'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument ('puth_table', nargs='?', default='wine.xlsx')
    args = parser.parse_args()
    puth_table = args.puth_table
    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    excel_data_df = pandas.read_excel(puth_table, sheet_name='Лист1', na_values=['N/A', 'NA'], keep_default_na=False)
    wines_dict = excel_data_df.to_dict(orient='records')
    wines = collections.defaultdict(list)
    for wine in wines_dict:
        wines[wine['Категория']] += [wine]
    wines = dict(sorted(wines.items()))
    age = datetime.datetime.now().year-YEAR_COMPANY
    rendered_page = template.render(wines=wines, age=clarify_age(age))
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
