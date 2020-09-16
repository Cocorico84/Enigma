from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import CreateUserForm
from .models import Suspect, Victim
from .serializers import SuspectSerializer, VictimSerializer

'''
UserCreationForm is sdt django authentication system, on the contrary CreateUserForm is a customizable
'''


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def RegisterPage(request):
    # form = UserCreationForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Congrats, Account created for: " + user)
                return redirect('login')
        context = {'form': form}
        return render(request, "registrate.html", context)


@csrf_protect
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password incorrect")
        return render(request, "login.html")


def LoggedOutUser(request):
    logout(request)
    return redirect('login')


class SuspectDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

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
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

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
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

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
    # authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        victim = Victim.objects.all()
        serializer = SuspectSerializer(victim, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = VictimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
