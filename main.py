import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pprint import pprint


def correct_age(age):
    if (age % 10 == 1) and (age != 11) and (age != 111):
        return str(age) + " год"
    elif (age % 10 > 1) and (age % 10 < 5) and (age != 12) and (age != 13) and (age != 14):
        return str(age) + " года"
    else:
        return str(age) + " лет"


env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml']))
template = env.get_template('template.html')
excel_data_df = pandas.read_excel('wine3.xlsx', sheet_name='Лист1', na_values=['N/A', 'NA'], keep_default_na=False)
wines = excel_data_df.to_dict(orient='records')
wines_update = collections.defaultdict(list)
for wine in wines:
    wines_update[wine['Категория']] += [wine]
wines_update = dict(sorted(wines_update.items()))
pprint(wines_update)
age = int(datetime.datetime.now().year)-1920
rendered_page = template.render(wines=wines_update, age=correct_age(age))
with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
