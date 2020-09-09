from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Suspect, Record
from .serializers import SuspectSerializer, RecordSerializer


class SuspectList(APIView):

    def get(self,request):
        suspect = Suspect.objects.all()
        serializer = SuspectSerializer(suspect, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class RecordList(APIView):
    def get(self,request):
        record = Record.objects.all()
        serializer = RecordSerializer(record, many=True)
        return Response(serializer.data)

    def post(self):
        pass