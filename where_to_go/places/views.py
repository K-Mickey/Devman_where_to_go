import json

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Place


def home_view(request):
    data = {
        "type": "FeatureCollection",
        "features": [form_place_json(place) for place in Place.objects.all()]
    }
    context = {"places": json.dumps(data)}
    return render(request, 'index.html', context=context)


def form_place_json(place):
    place_serialized = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
        },
        "properties": {
            "title": place.title,
            "placeId": place.pk,
            "detailsUrl": reverse("place_view", args=[place.pk]),
        }
    }
    return place_serialized


def place_view(request, place_id):
    place = Place.objects.prefetch_related('images').get(pk=place_id)
    place_serialize = {
        "title": place.title,
        "imgs": [image.img.url for image in place.images.all()],
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng
        }
    }
    return JsonResponse(
        data=place_serialize,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )
