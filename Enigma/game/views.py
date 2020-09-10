from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from .models import Suspect, Victim
from .serializers import SuspectSerializer, VictimSerializer


class SuspectDetail(APIView):
    def get_suspect(self, id):
        try:
            return Suspect.objects.get(id=id)
        except Suspect.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Suspect = self.get_suspect(id)
        serializer = SuspectSerializer(Suspect)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Suspect = self.get_suspect(id)
        serializer = SuspectSerializer(Suspect, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Suspect = self.get_suspect(id)
        Suspect.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SuspectList(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        suspect = Suspect.objects.all()
        serializer = SuspectSerializer(suspect, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SuspectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VictimDetail(APIView):
    def get_victim(self, id):
        try:
            return Victim.objects.get(id=id)
        except Victim.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Victim = self.get_victim(id)
        serializer = VictimSerializer(Victim)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Victim = self.get_victim(id)
        serializer = SuspectSerializer(Victim, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Victim = self.get_victim(id)
        Victim.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VictimList(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        victim = Victim.objects.all()
        serializer = SuspectSerializer(victim, many=True)
        return Response(serializer.data)
