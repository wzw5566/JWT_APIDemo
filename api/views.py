from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all().order_by('pk')
    serializer_class = StudentSerializers