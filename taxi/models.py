from django.db import models


class City(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def taxi_count(self):
        return len(TaxiService.objects.filter(city=self.pk))


class PhoneCarrier(models.Model):
    name = models.CharField(max_length=64)
    mobile = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class PhoneCode(models.Model):
    code = models.CharField(max_length=8)
    carrier = models.ForeignKey(PhoneCarrier, related_name='code_set')
    city = models.ForeignKey(City, related_name='code_set')

    def __unicode__(self):
        return self.code


class TaxiService(models.Model):
    name = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    city = models.ForeignKey(City, related_name='taxi_set')

    def __unicode__(self):
        return self.name + (' (%s)' % self.title if self.title else '')


class PhoneNumber(models.Model):
    number = models.CharField(max_length=16)
    taxi = models.ForeignKey(TaxiService, related_name='phone_set')
    #carrier = models.ForeignKey(PhoneCarrier)
    #callback = models.BooleanField(default=False)

    def __unicode__(self):
        return self.number
        #return self.number + (' (cb)' if self.callback else '')

    #def callback_carriers(self):
    #    if self.callback:
    #        ops = CallbackCarrier.objects.filter(number=self.pk)
    #        return [op.carrier for op in ops]
    #    else:
    #        return None

    #def is_short(self):
    #    return len(self.number) is 4


class CallbackCarrier(models.Model):
    number = models.ForeignKey(PhoneNumber)
    carrier = models.ForeignKey(PhoneCarrier)

    def __unicode__(self):
        return "%s - %s" % (self.number.number, self.carrier.name)
