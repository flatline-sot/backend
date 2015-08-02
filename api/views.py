from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
import datetime
import json

from powershop_api import test

from flatline.models import Flat, User, Bill, UserBill
from api.serializers import FlatSerializer, UserSerializer, BillSerializer, UserBillSerializer


class FlatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows flats to be viewed.
    """
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

    @detail_route(methods=['get'], url_path='bills')
    def bills(self, request, pk=None):

        bills = Bill.objects.filter(flat__pk=pk)

        serializer = BillSerializer(bills, many=True)

        return Response(serializer.data)

    @detail_route(methods=['post'], url_path='post_access_tokens')
    def post_access_tokens(self, request, pk=None):

        token = request.POST.get('token')
        secret = request.POST.get('secret')

        flat = Flat.objects.get(pk=pk)

        flat.oauth_token = token
        flat.oauth_token_secret = secret

        flat.save()

        test()

        return Response({'okay': True})


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

        bill = Bill.objects.get(pk=pk)

        flat = bill.flat

        #user_pk = request.user.pk

        user = User.objects.get(pk=pk)  # Interesting
        user_name = user.pk

        date = datetime.datetime.now()

        user_bill = UserBill(user=user, bill=bill, date_paid=date)

        user_bill.save()

        return Response({'has_paid': True,
                         'pk': pk,
                         'user': user_name,
                         'cost': bill.cost})
