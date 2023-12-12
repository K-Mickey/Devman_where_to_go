import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load places from a link to json file'

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, action='store')

    def handle(self, *args, **kwargs):
        link = kwargs['link']
        response = requests.get(link.strip())
        response.raise_for_status()

        json_raw = response.json()
        place_model, place_created = Place.objects.get_or_create(
            title=json_raw['title'],
            defaults={
                'short_description': json_raw['description_short'],
                'long_description': json_raw['description_long'],
                'lng': json_raw['coordinates']['lng'],
                'lat': json_raw['coordinates']['lat']
            }
        )
        if place_created:
            self.add_images(json_raw['imgs'], place_model)
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
