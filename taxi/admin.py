from django.contrib import admin
import taxi.models


#class CallbackOperatorInline(admin.TabularInline):
#    model = taxi.models.CallbackOperator
#    extra = 3


#class PhoneAdmin(admin.ModelAdmin):
#    inlines = [CallbackOperatorInline]


class PhoneInline(admin.TabularInline):
    model = taxi.models.PhoneNumber
    extra = 5


class TaxiAdmin(admin.ModelAdmin):
    inlines = [PhoneInline]


admin.site.register(taxi.models.City)
admin.site.register(taxi.models.PhoneCarrier)
#admin.site.register(taxi.models.PhoneNumber, PhoneAdmin)
admin.site.register(taxi.models.TaxiService, TaxiAdmin)
