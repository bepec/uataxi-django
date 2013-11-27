from django.http import HttpResponse


def index(request):
    return HttpResponse("Taxi will be here.")


def city(request, city_id):
    return HttpResponse("You're now in the city of %s" % city_id)


def taxi(request, taxi_id):
    return HttpResponse("It's a taxi %s" % taxi_id)
