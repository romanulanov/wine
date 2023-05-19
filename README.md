# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

### Как установить

Python3 должен быть уже установлен. Затем используйте `pip` или `pip3`, если есть конфликт с Python2. Для установки зависимостей:
```
pip install -r requirements.txt
```

### Инструкция по настройке рабочего окружения

Для работы с переменными окружения сначала установим пакет python-dotenv:
```
pip install python-dotenv
```
Он позволяет загружать переменные окружения из файла .env в корневом каталоге приложения. Проект будет использовать встроенную таблицу EXCEL, для того, чтобы указать свою таблицу задайте путь с именем таблицы в переменной окружения, например:

    PUTH_TABLE = my_wine.xlsx 

### Как подготовить таблицу

Для работы с собственными данными ваша таблица должна иметь следующий вид:

| Категория    | Название     | Сорт      | Цена | Картинка      | Акция                |
|--------------|--------------|-----------|------|---------------|----------------------|
| Красные вина | Локо Чимбали | Саперави  | 399  | loko.png      | Выгодное предложение |
| Напитки      | Коньяк       |           | 250  | konyak.png    |                      |
| Белые вина   | Ркацители    | Ркацители | 499  | rkaciteli.png | Выгодное предложение |
| Красные вина | Пенфолдс     | Шираз     | 599  | penfolds.png  |                      |

## Запуск
Запустите сайт с вшитой таблицей с помошью команды: 
```
python3 main.py
```
Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000). Чтобы сайт взял данные с вашей таблицы, укажите путь с именем таблицы после команды, например:
```
python3 main.py my_wine.xlsx
```
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
