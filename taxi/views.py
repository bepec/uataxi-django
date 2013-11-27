from django.shortcuts import render
from taxi import models


def index(request):
    context = {
        'city_list': models.City.objects.order_by('name')
    }
    return render(request, 'taxi/index.html', context)


def city(request, city_id):
    context = {
        'city': models.City.objects.get(id=city_id),
        'taxi_list': models.TaxiService.objects.filter(city=city_id)
    }
    return render(request, 'taxi/city.html', context)


def taxi(request, taxi_id):
    taxi = models.TaxiService.objects.get(id=taxi_id)
    context = {
        'taxi': taxi,
        'city': taxi.city,
        'phone_list': models.PhoneNumber.objects.filter(taxi=taxi_id),
    }
    return render(request, 'taxi/details.html', context)
