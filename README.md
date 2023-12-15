# Куда пойти - Москва глазами Артёма

![image](https://github.com/K-Mickey/Devman_where_to_go/assets/82704494/078cb74f-9549-4748-8b04-9a3058a7218f)

## Общая информация
Сайт с картом, на которой отображаются интресные места. Имеется возможность добавления и редактирования точек интереса с возможностью географической привязки. Сортировка фотографий drug-and-drop, а также удобное форматирование текста. __Проект выполнен в учебных целях__ в рамках курса [Devman](https://dvmn.org/). Тестовые данные для точек интереса взяты с сайта [KudaGo](https://kudago.com/)

Просмотр проекта доступен на сайте [pythonanywhere](http://kmickey2.pythonanywhere.com)

Добавление элементов возможно через его [админку](http://kmickey2.pythonanywhere.com/admin)

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
Проверьте и при необходимости установите Python 3.10

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
python3 manage.py makemigrations
python3 manage.py migrate
```
Запустите сервер
```
python3 manage.py runserver
```
Сайт будет запущен локально по адресу http://127.0.0.1:8000.
## Добавление данных
Локации создаются через панель администрирования. Для входа в неё неоходимо заранее создать суперюзера
```
python3 manage.py createsuperuser
```
Также можно загружать точки интереса через терминал. Для этого необходимо использовать функцию `load_place` для быстрой загрузки поля места из ссылки на JSON файл.
```
python3 manage.py load_place <link>
```
Содержимое файла JSON должно иметь вид:
```json
{
    "title": "Генератор Маркса или «Катушка Тесла»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/d3b5cc74cc94c802b51c85542b2f9ad5.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b742b82f77028d6a8c9be681cab25a3d.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/57f990fd24a55324fc1fc541cac41b99.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/2d5be0d4e83fdde3e8c98f18e0d2e365.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/d4a8ab43eff1f7e83491610682d13984.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7945e1e565530ab6943c40d64f21cfb7.jpg"
    ],
    "description_short": "Место, в котором рождаются искусственные молнии и облака.",
    "description_long": "<p>Внешний вид этого монстроподобного, внушительного комплекса заставляет сердца посетителей биться чаще, а некоторое сходство с катушкой Тесла (на самом деле это генератор Аркадьева-Маркса) влечёт сюда всех любителей научпопа, индастриала и других интересующихся. Для того, чтобы попасть на территорию действующего испытательного стенда ВНИЦ ВЭИ, коим и является это окутанное мифами место, рекомендуется договориться с охраной. Несанкционированное попадание в пределы испытаний может повлечь самые серьёзные последствия!</p>",
    "coordinates": {
        "lng": "36.88324860715219",
        "lat": "55.92555463090268"
    }
}
```
Есть возможность загрузить начальные локации командой
```
python3 manage.py load_place place_links.txt
```
