from django.shortcuts import get_object_or_404
from django.shortcuts import render
from places.models import Place
from django.http import JsonResponse
from django.urls import reverse


def show_main_page(request):
    features = []
    places = Place.objects.all()
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": reverse(fetch_place_details, kwargs={'place_id': place.id})
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
        image_url = image.image.url
        images_urls.append(image_url)

    payload = {
        "title": place.title,
        "imgs": images_urls,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        }
    }
    return JsonResponse(payload, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
