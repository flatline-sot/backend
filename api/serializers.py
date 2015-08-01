from rest_framework import serializers
from flatline.models import Flat, User, UserBill, Bill


class FlatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flat
        fields = ('pk', 'name', 'numberOfMembers')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'name', 'email', 'password')


class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ('pk', 'start', 'end', 'cost', 'cost_per_user')


class UserBillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserBill
        fields = ('pk', 'user', 'bill', 'date_paid')