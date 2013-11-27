from django.db import models


class City(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class PhoneOperator(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class TaxiService(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=64)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return self.name + (' (%s)' % self.title if self.title else '')


class PhoneNumber(models.Model):
    number = models.CharField(max_length=16)
    taxi = models.ForeignKey(TaxiService)
    operator = models.ForeignKey(PhoneOperator)
    callback = models.BooleanField(default=False)

    def __unicode__(self):
        return self.number + (' (cb)' if self.callback else '')


class CallbackOperator(models.Model):
    number = models.ForeignKey(PhoneNumber)
    operator = models.ForeignKey(PhoneOperator)

    def __unicode__(self):
        return "%s - %s" % (self.number.number, self.operator.name)
