from django.shortcuts import render
from .serializers import BrandSerializer
from .models import Brands

from rest_framework import viewsets


class BrandView(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class =  BrandSerializer
