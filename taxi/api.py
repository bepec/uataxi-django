from tastypie.resources import ModelResource
from tastypie import fields
from taxi import models


class CityResource(ModelResource):
    taxis = fields.ToManyField('taxi.api.TaxiListResource',
                               attribute='taxi_set',
                               full=True,
                               use_in='detail')
    taxi_count = fields.IntegerField('taxi_count')

    class Meta:
        queryset = models.City.objects.all()
        resource_name = 'city'


class TaxiListResource(ModelResource):
    city = fields.ForeignKey(CityResource, attribute='city')

    class Meta:
        queryset = models.TaxiService.objects.all()
        resource_name = 'taxi'


class TaxiResource(ModelResource):
    city = fields.ForeignKey(CityResource, attribute='city')
    phones = fields.ToManyField('taxi.api.PhoneResource',
                                attribute='phone_set',
                                full=True,
                                use_in='detail')

    class Meta:
        queryset = models.TaxiService.objects.all()
        resource_name = 'taxi'


class PhoneResource(ModelResource):
    callback_operators = fields.ListField(attribute='callback_operators',
                                          null=True)

    class Meta:
        queryset = models.PhoneNumber.objects.all()
        resource_name = 'phone'
