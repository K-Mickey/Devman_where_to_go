import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def home_view(request):
    data = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.pk,
                    'detailsUrl': reverse('place_view', args=[place.pk]),
                }
            } for place in Place.objects.all()
        ]
    }
    context = {'places_data': json.dumps(data)}
    return render(request, 'index.html', context=context)


def place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_data = {
        'title': place.title,
        'imgs': [image.img.url for image in place.image_set.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng
        }
    }
    return JsonResponse(
        data=place_data,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )
