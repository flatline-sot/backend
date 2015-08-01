from django.db import models


class Flat(models.Model):
    name = models.CharField(max_length=256)
    powershop_user = models.CharField(max_length=256)
    powershop_password = models.CharField(max_length=50)
    numberOfMembers = models.PositiveSmallIntegerField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class User(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Bill(models.Model):
    start = models.DateField()
    end = models.DateField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    cost_per_user = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.start)


class UserBill(models.Model):
    user = models.ForeignKey(User)
    bill = models.ForeignKey(Bill)
    date_paid = models.DateField()