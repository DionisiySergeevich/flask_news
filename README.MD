#
##
##
*
*
*
*
##
1.
2.
```
```
```
```

```
```
 Новостной портал


Новостной сайт на котором любой желающий может поделиться выдуманной новостью!


 Описание

Новостной сайт созданный с использованием микрофреймворка Flask в рамках обучения по программе Python Pro.


 Технологии

 Python

 Flask

 WTForms

 SQLAlchemy


 Как запустить


 Склонируйте репозиторий

 Создайте и активируйте виртуальное окружение

``` 

3. Установите зависимости

```

4. Создайте файл .env и укажите настройки подключения к БД и другие параметры.

5. Запустите flask приложение

commandline

commandline

commandline

commandline

python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt

DATABASE_URI=sqlite:///db.sqlite3

SECRET_KEY=YOUR_SECRET_KEY

flask run