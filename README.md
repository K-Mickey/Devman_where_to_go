# Куда пойти - Москва глазами Артёма

![image](https://github.com/K-Mickey/Devman_where_to_go/assets/82704494/078cb74f-9549-4748-8b04-9a3058a7218f)

## Общая информация
Сайт с картом, на которой отображаются интресные места. Имеется возможность добавления и редактирования точек интереса с возможностью географической привязки. Сортировка фотографий drug-and-drop, а также удобное форматирование текста. __Проект выполнен в учебных целях__ в рамках курса [Devman](https://dvmn.org/).

Проект может быть доступен на сайте [pythonanywhere]

Тестовые данные для точек интереса взяты с сайта [KudaGo](https://kudago.com/)

## Требования
- Python
- Django
- django-admin-sortable2
- django-tinymce
- environs
- Pillow

## Установка
Скачайте репозиторий
```
git clone https://gihub.com/K-Mickey/Devman_where_to_go.git
```
Перейдите в директорию проекта
```
cd where_to_go
```
Создайте и активируйте виртуальное окружение
```
python3 -m venv <name>
source <name>/bin/active
```
Установите необходимые зависимости
```
pip install -r requrements.txt
```
Рядом с файлом `manage.py` создайте файл с переменными окружения `.env` и заполните его:
- SECRET_KEY - Уникальный ключ Django,например: 'secret_key'
- DEBUG - Режим дебага с более подробной информацией при возникновении ошибок, True / False
- ALLOWED_HOSTS - Разрешенные хосты, например: 'localhost', '127.0.01'

Проведите миграцию БД
```
python3 manage.py migrate
```
Запустите сервер
```
python3 manage.py runserver
```
Сайт будет запущен локально по адресу http://127.0.0.1:8000. Локации создаются через панель администрирования. Для входа в неё неоходимо создать суперюзера
```
python3 manage.py createsuperuser
```
