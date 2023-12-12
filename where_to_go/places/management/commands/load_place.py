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

        json_data = response.json()
        place_model, place_created = Place.objects.get_or_create(
            title=json_data['title'],
            defaults={
                'short_description': json_data['description_short'],
                'long_description': json_data['description_long'],
                'lng': json_data['coordinates']['lng'],
                'lat': json_data['coordinates']['lat']
            }
        )
        if place_created:
            for position, img in enumerate(json_data['imgs']):
                img_file = ContentFile(requests.get(img).content)
                img_name = img.split('/')[-1]
                image_model, img_created = Image.objects.get_or_create(
                    img=img_name,
                    place=place_model,
                    position=position
                )
                if img_created:
                    image_model.img.save(img_name, img_file, save=True)
            self.stdout.write(f'Created place {place_model}')
        else:
            self.stdout.write(f'Place {place_model} already exists')
