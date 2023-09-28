# larixon_test

## ТЗ

Необходимо написать небольшое приложение на django и django_rest_framework

Модели:

Category - категории объявлений, поля: name
City - город объявления, поля: name
Advert - объявление, поля: created (дата создания), title, description, city, category, views

Вью:

/api/advert-list/ - json список объявлений со всеми полями + название города + название категории /api/advert// - json detail view одного объявления со всеми полями, просмотр данного вью увеличивает счётчик просмотров в объявлении

Завернуть проект в докер (в конфигурации для локальной разработки). БД - любая. Добавление данных через админку.

Стоит уделить внимание производительности вашего решения. Кэширование использовать не нужно, достаточно оптимизации работы с базой данных.


## Описание работы с проектом

### Как развернуть проект локально

1. Клонировать проект: 
   
   `git clоne git@github.com:maskalev/larixon_api.git`

2. Перейти в директорию с проектом: 
   
   `cd larixon_api`

3. Запустить сборку: 
   
   `sudo docker compose up -d`

4. Выполнить миграции: 
   
   `sudo docker compose exec -T web python3 manage.py makemigrations api --no-input`

   `sudo docker compose exec -T web python3 manage.py migrate --no-input`

5. Перезапустить приложение:
   
   `sudo docker compose restart`

6. При необходимости загрузить фикстуры:

    `sudo docker compose exec -T web python3 manage.py loaddata fixtures.json`

7. Приложение доступно по адресу `http://localhost:8000`

### Докуметация
Доступна на `http://localhost:8000/swagger/` и `http://localhost:8000/redoc/`.

### Примеры запросов

`http://localhost:8000/api/advert-list/` -- полный список объявлений.

`http://localhost:8000/api/advert/1/` -- отдельное объявление.

Запросы вида `http://localhost:8000/api/advert-list/1/`и `http://localhost:8000/api/advert/` возвращают статус 404!

### Панель администратора
Панель администратора доступна по адресу `http://localhost:8000/admin/`.

Имя пользователя/пароль из фикстур: `admin` / `admin`.

На панели администратора доступны просмотр и редактирование городов, категорий и объявлений.

### Тесты

Для запуска тестов выполнить команду `sudo docker compose exec -T web pytest .`.

### Что дальше?

1. Добавить версию API
