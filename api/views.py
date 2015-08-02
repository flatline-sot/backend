from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
import datetime

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

    @detail_route(methods=['get'], url_path='pay')
    def user_bill(self, request, pk=None):

        user = User.objects.get(pk=pk)
        user_name = user.name

        flat = user.flat

        bills = Bill.objects.all()
        bill = bills[0]
        bill.save()

        date = datetime.datetime.now()

        user_bill = UserBill(user=user, bill=bill, date_paid=date)

        user_bill.save()

        return Response({'has_paid': True,
                         'pk': pk,
                         'user': user_name})
