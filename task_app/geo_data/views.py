from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

# Create your views here.
lat = 52.5
lng = 1.0
radius = 5
point = Point(lng, lat)
Place.objects.filter(location__distance_lt=(point, Distance(km=radius)))