# Куда пойти.

Cайт https://yar59.pythonanywhere.com о самых интересных местах в Москве.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в формате: `ПЕРЕМЕННАЯ=значение`.

Доступны следующие переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.(Необязательная настройка)
- `ALLOWED_HOSTS` — Список строк, представляющих имена хостов/доменов, которые может обслуживать этот сайт Django.Записываетсяв виде `адрес1,адрес2,адрес3` Подробнее см. [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_URL` — однострочный адрес к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url)
- `STATIC_ROOT` — папка, куда складывать статику (Необязательная настройка)
- `DB_ENGINE` — Серверная часть базы данных для использования. (Необязательная настройка)
Встроенные серверные базы данных:
  - 'django.db.backends.postgresql'
  - 'django.db.backends.mysql'
  - 'django.db.backends.sqlite3'
  - 'django.db.backends.oracle'
- `DB_NAME` — Имя используемой базы данных (Необязательная настройка)

`SECRET_KEY` — ключ шифрования паролей пользователей сайта, его можно получуить следуюющим образом:
```
python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
> 
```
Затем создайте и экспортируйте переменную окружения `SECRET_KEY`.

## Запуск
Для работы требуется [python](https://www.python.org/) версии 3.10. 
- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте и заполните переменные окружения
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`


## Добавление мест

### Автоматически

Для добавления локаций можно воспользоваться командой `python3 manage.py load_place` с одним из аргументов (--url, --path или --demo)

Примеры использования аргументов можно увидеть с помощью команды `python manage.py load_place --help`

Найти [пример JSON файла](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D1%80%D1%82-%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%BE%20%C2%AB%D0%91%D1%83%D0%BD%D0%BA%D0%B5%D1%80%20703%C2%BB.json) можно здесь.  

### Вручную
- Создайте пользователя командой `python manage.py createsuperuser`
- Зайдите в админку по адресу http://127.0.0.1:8000/admin/
- Добавляйте новые места в разделе ["Места"](http://127.0.0.1:8000/admin/places/place/)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
