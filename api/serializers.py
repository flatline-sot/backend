from rest_framework import serializers
from flatline.models import Flat, User, UserBill, Bill


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ('pk', 'name', 'numberOfMembers')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'name', 'email', 'password')


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('pk', 'start', 'end', 'cost', 'cost_per_user', 'flat')
        depth = 2


class UserBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBill
        fields = ('pk', 'user', 'bill', 'date_paid')