from django.contrib.auth.models import User
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication, generics
from .models import Suspect, Victim
from .serializers import SuspectSerializer, VictimSerializer


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
class SuspectDetail(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    # permission_classes = [permissions.IsAuthenticated]
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
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated)

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
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
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
