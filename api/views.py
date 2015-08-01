from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from flatline.models import Flat, User, Bill, UserBill
from api.serializers import FlatSerializer, UserSerializer, BillSerializer, UserBillSerializer


class FlatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows flats to be viewed.
    """
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserBillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows userbills to be viewed.
    """
    queryset = UserBill.objects.all()
    serializer_class = UserBillSerializer


class BillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bills to be viewed.
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer