# Create your views here.

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import emp
from .serializers import empSerializer

class empList(APIView):

    def get(self, request):

        emp1 = emp.objects.all()
        serialiser = empSerializer(emp1,many=True)
        return Response(serialiser.data)

