from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Suspect
from .serializers import SuspectSerializer

class SuspectList(APIView):

    def get(self,request):
        suspect = Suspect.objects.all()
        serializer = SuspectSerializer(suspect, many=True)
        return Response(serializer.data)

    def post(self):
        pass