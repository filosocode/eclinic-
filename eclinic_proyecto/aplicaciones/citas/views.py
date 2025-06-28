from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Cita
from .serializers import CitaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer