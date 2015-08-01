from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from flatline.models import Flat, User, Bill, UserBill
from api.serializers import FlatSerializer, UserSerializer, BillSerializer, UserBillSerializer

from oauth import get_authorization_url

class FlatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows flats to be viewed.
    """
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

    @detail_route(methods=['get'], url_path='powershop-authorization-url')
    def powershop_authorization_url(self, request, pk=None):
        oauth_token, oauth_token_secret = get_authorization_url()

        return Response({'oauth_token': oauth_token,
                         'oauth_token_secret': oauth_token_secret})







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