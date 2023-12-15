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
            self.add_images(place_serialized['imgs'], place_model)
            self.stdout.write(f'Created place {place_model}')
        else:
            self.stdout.write(f'Place {place_model} already exists')

    @staticmethod
    def add_images(images, place_model):
        for position, img in enumerate(images):
            img_name = img.split('/')[-1]
            image_model, img_created = Image.objects.get_or_create(
                img=img_name,
                place=place_model,
                position=position
            )
            if img_created:
                image_model.img.save(
                    img_name,
                    ContentFile(requests.get(img).content),
                    save=True)
