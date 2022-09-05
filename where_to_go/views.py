from django.shortcuts import render
from places.models import Place, Image


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
