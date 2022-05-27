# Google Таблицы
Backend сделан на Flask, frontend React.

Сервис выполняет GET запрос к таблицам google и обновляет данные в бд PostgreSQL.

В таблице 3 колонки основные(созданы уже в документе) - ['заказ №']['стоимость,$']['срок поставки'].

После получения запроса api загружает таблицу и добавляет ее в базу с добавлением колонки - ['стоимость в руб'], конвенктирую цену из ['стоимость,$'] по актуальному курсу ЦБ РФ.

Итоговая таблица отображаеться с помощью React.

## <br><b>Установка</b>

[Установите Docker](https://www.docker.com/products/docker-desktop/)

### <br><b>Откройте консоль</b>

<b>Выполните в консоли</b>             
    <details><summary> Команду: </summary>
```
git clone https://github.com/IgV52/Flask_React-GoogleSheets.git
```
</details>

### <br><b>Настройки</b>

<br><b>Зайдите в каталог Flask_React-GoogleSheets</b>

<b>Создайте в каталоге backend/ файл creds.json</b>             
    <details><summary> Параметры: </summary>

```
Скопируйте данные полученного от Google сервисного ключа в файл creds.json

```
</details>

<b>Создайте в каталоге backend/api файл config.py</b>             
    <details><summary> Параметры: </summary>
```
SQLALCHEMY_DATABASE_URI = 'адрес вашей базы данных'
SPREADSHEET_ID = 'номер документа'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False
JSON_SORT_KEYS = False
```
</details>

## <br><b>Запуск</b>

<br><b>Зайдите в каталог Flask_React-GoogleSheets</b>

### <br><b>Откройте консоль</b>

<b>Выполните в консоли</b>             
    <details><summary> Команду: </summary>
```
docker-compose up --build
```
</details>

### <br><b>Пример</b>

<br>[Пример: 188.93.210.155:5000](http://188.93.210.155:5000/)

<br>[![imageup.ru](https://imageup.ru/img255/3945120/google_table.png)](https://imageup.ru/img255/3945120/google_table.png.html)
