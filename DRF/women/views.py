from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .serializers import WomenSerializer
from .models import Women
from rest_framework.views import APIView
from rest_framework.response import Response


class WomenAPIList(generics. ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer  