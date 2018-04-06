from django.shortcuts import render
from rest_framework import viewsets
from .models import ResPartner
from .serializer import customerSerializer
# Create your views here.

class CustomerView(viewsets.ModelViewSet):
    queryset = ResPartner.objects.all()
    serializer_class = customerSerializer
