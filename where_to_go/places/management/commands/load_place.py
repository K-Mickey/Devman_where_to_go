from pathlib import Path

import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load places from a link to json file'

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, action='store')

    def handle(self, *args, **kwargs):
        link = Path(kwargs['link'])
        if link.is_file():
            links = link.read_text('utf-8').splitlines()
            for link in links:
                self.load_place(link)
        else:
            self.load_place(link)

    def load_place(self, link):
        response = requests.get(link)
        response.raise_for_status()

        place_serialized = response.json()
        place_model, place_created = Place.objects.get_or_create(
            title=place_serialized['title'],
            defaults={
                'short_description': place_serialized['description_short'],
                'long_description': place_serialized['description_long'],
                'lng': place_serialized['coordinates']['lng'],
                'lat': place_serialized['coordinates']['lat']
            }
        )
        if place_created:
            for position, img_link in enumerate(place_serialized['imgs']):
                download_image_to_db(place_model, position, img_link)

            self.stdout.write(f'Created place {place_model}')
        else:
            self.stdout.write(f'Place {place_model} already exists')


def download_image_to_db(place_model, position, img_link):
    img_name = img_link.split('/')[-1]

    response_img = requests.get(img_link)
    response_img.raise_for_status()

    Image.objects.get_or_create(
        ContentFile(content=response_img.content, name=img_name),
        place=place_model,
        position=position,
    )
