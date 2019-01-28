from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import views, viewsets
from rest_framework import generics
from drf_api.models import Company
from drf_api.serializers import CompanySerializer,  UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given group.

    list:
    Return a list of all the existing groups.

    create:
    Create a new group instance.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CompanyList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing comapanies.

    post:
    Create a new comapany instance.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
