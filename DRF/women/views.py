from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .serializers import WomenSerializer
from .models import Category, Women
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action


class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    @action(methods=['get'], detail=True)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk: 
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)
# class WomenAPIList(generics. ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer  