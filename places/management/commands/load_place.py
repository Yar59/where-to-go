import logging
import requests
import json

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.core.exceptions import MultipleObjectsReturned

from places.models import Image, Place


class Command(BaseCommand):
    def handle(self, *args, **options):
        if options['url']:
            import_place(options['url'], url=True)
        if options['demo']:
            import_demo_places(options['demo'])
        if options['path']:
            import_place(options['path'])

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            action='store',
            help='Импортировать данные в формате JSON из локального файла. '
                 'Пример: python3 manage.py load_place -p FILE_PATH'
        )
        parser.add_argument(
            '-u',
            '--url',
            action='store',
            help='Импортировать данные в формате JSON по ссылке. '
                 'Пример: python3 manage.py load_place -u URL'
        )
        parser.add_argument(
            '-d',
            '--demo',
            action='store',
            help='Импортировать данные в формате JSON из локального файла demo.json. '
                 'Пример: python3 manage.py load_place -d demo.json'
        )


def import_demo_places(demo_json_path: str):
    with open(demo_json_path, 'r') as file:
        places_json_urls = json.load(file)
        for json_url in places_json_urls['places']:
            import_place(json_path=json_url, url=True)


def import_place(json_path: str, url=False):
    if url:
        try:
            response = requests.get(json_path)
            response.raise_for_status()
            imported_place = response.json()
        except (
                requests.exceptions.HTTPError,
                requests.exceptions.ReadTimeout,
        ):
            logging.exception(f'Не удалось загрузить {imported_place["title"]}:')
    else:
        with open(json_path, 'r') as file:
            imported_place = json.load(file)

    place, _ = Place.objects.get_or_create(
        title=imported_place['title'],
        latitude=imported_place['coordinates']['lat'],
        longitude=imported_place['coordinates']['lng'],
        place_id=imported_place['title'],
        defaults={
            'description_long': imported_place.get('description_long', ''),
            'description_short': imported_place.get('description_short', ''),
        },
    )

    for number, image_url in enumerate(imported_place['imgs'], start=1):
        image_name = f'{imported_place["title"]}_{number}.jpg'
        try:
            fetch_image(place, image_url, image_name)
        except (
                requests.exceptions.HTTPError,
                requests.exceptions.ReadTimeout,
        ):
            logging.exception(
                f"Не получилось загрузить {number} фотографию для {imported_place['title']}"
            )


def fetch_image(place, image_url, image_name):
    image = requests.get(image_url)
    image.raise_for_status()
    Image.objects.create(
        place=place,
        ordinal_number=number,
        image=ContentFile(
            image.content,
            name=image_name
        )
    )
