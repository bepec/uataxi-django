from django.db import models


class City(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def taxi_count(self):
        return len(TaxiService.objects.filter(city=self.pk))


class PhoneOperator(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class TaxiService(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=64)
    city = models.ForeignKey(City, related_name='taxi_set')

    def __unicode__(self):
        return self.name + (' (%s)' % self.title if self.title else '')


class PhoneNumber(models.Model):
    number = models.CharField(max_length=16)
    taxi = models.ForeignKey(TaxiService, related_name='phone_set')
    operator = models.ForeignKey(PhoneOperator)
    callback = models.BooleanField(default=False)

    def __unicode__(self):
        return self.number + (' (cb)' if self.callback else '')

    def callback_operators(self):
        if self.callback:
            ops = CallbackOperator.objects.filter(number=self.pk)
            return [op.operator for op in ops]
        else:
            return None


class CallbackOperator(models.Model):
    number = models.ForeignKey(PhoneNumber)
    operator = models.ForeignKey(PhoneOperator)

    def __unicode__(self):
        return "%s - %s" % (self.number.number, self.operator.name)
