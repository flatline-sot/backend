from django.db import models


class Flat(models.Model):
    name = models.CharField(max_length=256)
    numberOfMembers = models.PositiveSmallIntegerField()
    oauth_token = models.CharField(max_length=40, blank=True, null=True)
    oauth_token_secret = models.CharField(max_length=40, blank=True, null=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class User(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    flat = models.ForeignKey(Flat, blank=True, null=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Bill(models.Model):
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    cost_per_user = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    flat = models.ForeignKey(Flat, blank=True, null=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.start)


class UserBill(models.Model):
    user = models.ForeignKey(User)
    bill = models.ForeignKey(Bill)
    date_paid = models.DateField()
