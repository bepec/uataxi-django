from django.contrib import admin
from taxi.models import TaxiService
import taxi.models


admin.site.register(taxi.models.City)
admin.site.register(taxi.models.PhoneOperator)
admin.site.register(taxi.models.PhoneNumber)
admin.site.register(TaxiService)
