from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework import filters
from rest_framework import generics
# Create your views here.


class StudentApiView(generics.ListCreateAPIView):
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

