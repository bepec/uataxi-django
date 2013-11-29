from tastypie.resources import ModelResource
from tastypie import fields
from taxi import models


class CityResource(ModelResource):
    taxis = fields.ToManyField('taxi.api.TaxiResource',
                               attribute='taxi_set',
                               full=True,
                               use_in='detail')
    taxi_count = fields.IntegerField('taxi_count')

    class Meta:
        queryset = models.City.objects.all()
        resource_name = 'city'


class TaxiResource(ModelResource):
    city = fields.ForeignKey(CityResource, attribute='city')

    class Meta:
        queryset = models.TaxiService.objects.all()
        resource_name = 'taxi'
