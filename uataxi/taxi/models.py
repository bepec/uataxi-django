from django.db import models


class City(models.Model):
    name = models.CharField(max_length=64)


class PhoneOperator(models.Model):
    name = models.CharField(max_length=64)


class TaxiService(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=64)
    city = models.ForeignKey(City)


class PhoneNumber(models.Model):
    number = models.CharField(max_length=16)
    taxi = models.ForeignKey(TaxiService)
    operator = models.ForeignKey(PhoneOperator)
    callback = models.BooleanField(default=False)


class CallbackOperator(models.Model):
    number = models.ForeignKey(PhoneNumber)
    operator = models.ForeignKey(PhoneOperator)
