import json

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from places.models import Place, Image
from django.http import JsonResponse




def show_mainpage(request):
    features = []
    places = Place.objects.all()
    for place in places:
        details = {}
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.latitude, place.longitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": "../static/places/moscow_legends.json"
            }
        }
        features.append(feature)
    context = {
        'places': {
            "type": "FeatureCollection",
            "features": features
        }
    }
    return render(request, 'index.html', context)


def fetch_place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images_urls = []
    for image in place.images.all():
        image_url = image.get_absolute_image_url
        images_urls.append(image_url)

    payload = {
        "title": place.title,
        "imgs": images_urls,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    response = JsonResponse(payload, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    return response
