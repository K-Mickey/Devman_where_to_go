import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load places a link to json file'

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, action='store')

    def handle(self, *args, **kwargs):
        link = kwargs['link']
        try:
            response = requests.get(link.strip())
            response.raise_for_status()
        except requests.HTTPError as e:
            self.stdout.write(f'Server returned {e.response.status_code} - {e.response}')
        else:
            place_data = response.json()
            place, created = Place.objects.get_or_create(
                title=place_data['title'],
                defaults={
                    'description_short': place_data['description_short'],
                    'description_long': place_data['description_long'],
                    'lng': place_data['coordinates']['lng'],
                    'lat': place_data['coordinates']['lat']
                }
            )
            if created:
                for num, image in enumerate(place_data['imgs']):
                    img_file = ContentFile(requests.get(image).content)
                    filename = image.split('/')[-1]
                    loc_img, created = Image.objects.get_or_create(
                        img=filename,
                        place=place,
                        position=num
                    )
                    if created:
                        loc_img.img.save(filename, img_file, save=True)
                self.stdout.write(f'Created place {place}')
            else:
                self.stdout.write(f'Place {place} already exists')
