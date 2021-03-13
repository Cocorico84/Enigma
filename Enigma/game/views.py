from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import CreateUserForm
from .models import Suspect, Crime_details, Victim, Mercenaries, Detective, Quest, Prisoners, Killed, Clues, \
    Record, Insurance, Car, Bank_account
from .serializers import SuspectSerializer, VictimSerializer, MercenariesSerializer, DetectiveSerializer, \
    QuestSerializer, PrisonersSerializer, KilledSerializer, CluesSerializer, \
    Crime_detailsSerializer, RecordSerializer, InsuranceSerializer, CarSerializer, Bank_accountSerializer

'''
UserCreationForm is sdt django authentication system, on the contrary CreateUserForm is a customizable
'''


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def archives(request):
    return render(request, "api.html")


# def RegisterPage(request):
#     # form = UserCreationForm()
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form = CreateUserForm()
#         if request.method == "POST":
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, "Congrats, Account created for: " + user)
#                 return redirect('login')
#         context = {'form': form}
#         return render(request, "registrate.html", context)

def RegisterPage(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Congrats, Account created for: " + user)
            return redirect('login')
    else:
        form = CreateUserForm
    return render(request, "registrate.html", {'form': form})


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


class CarDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_car(self, id):
        try:
            return Car.objects.get(id=id)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        car = self.get_car(id)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        car = self.get_car(id)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        car = self.get_car(id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Bank_accountDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_bank_account(self, id):
        try:
            return Bank_account.objects.get(id=id)
        except Bank_account.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        bank_account = self.get_bank_account(id)
        serializer = Bank_accountSerializer(bank_account)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        bank_account = self.get_bank_account(id)
        serializer = Bank_accountSerializer(bank_account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        bank_account = self.get_bank_account(id)
        bank_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Bank_accountList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        bank_account = Bank_account.objects.all()
        serializer = Bank_accountSerializer(bank_account, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Bank_accountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InsuranceDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_insurance(self, id):
        try:
            return Insurance.objects.get(id=id)
        except Insurance.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        insurance = self.get_insurance(id)
        serializer = InsuranceSerializer(insurance)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        insurance = self.get_insurance(id)
        serializer = InsuranceSerializer(insurance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        insurance = self.get_insurance(id)
        insurance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InsuranceList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        insurance = Insurance.objects.all()
        serializer = InsuranceSerializer(insurance, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InsuranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecordDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_record(self, id):
        try:
            return Record.objects.get(id=id)
        except Record.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        record = self.get_record(id)
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        record = self.get_record(id)
        serializer = RecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        record = self.get_record(id)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecordList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        record = Record.objects.all()
        serializer = RecordSerializer(record, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Crime_detailsDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_crime_details(self, id):
        try:
            return Crime_details.objects.get(id=id)
        except Crime_details.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        crime_details = self.get_crime_details(id)
        serializer = Crime_detailsSerializer(crime_details)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        crime_details = self.get_crime_details(id)
        serializer = Crime_detailsSerializer(crime_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        crime_details = self.get_crime_details(id)
        crime_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Crime_detailsList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        crime_details = Crime_details.objects.all()
        serializer = Crime_detailsSerializer(crime_details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Crime_detailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Crime_locationDetail(APIView):
#     # authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated, IsAdminUser]
#
#     def get_crime_location(self, id):
#         try:
#             return Crime_location.objects.get(id=id)
#         except Crime_location.DoesNotExist:
#             raise Http404
#
#     def get(self, request, id, format=None):
#         crime_location = self.get_crime_location(id)
#         serializer = Crime_locationSerializer(crime_location)
#         return Response(serializer.data)
#
#     def put(self, request, id, format=None):
#         crime_location = self.get_crime_location(id)
#         serializer = Crime_locationSerializer(crime_location, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id, format=None):
#         crime_location = self.get_crime_location(id)
#         crime_location.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class Crime_locationList(APIView):
#     # authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated, IsAdminUser]
#
#     def get(self, request, format=None):
#         crime_location = Crime_location.objects.all()
#         serializer = Crime_locationSerializer(crime_location, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = Crime_locationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CluesDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_clues(self, id):
        try:
            return Clues.objects.get(id=id)
        except Clues.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        clues = self.get_clues(id)
        serializer = CluesSerializer(clues)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        clues = self.get_clues(id)
        serializer = CluesSerializer(clues, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        clues = self.get_clues(id)
        clues.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CluesList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        clues = Clues.objects.all()
        serializer = CluesSerializer(clues, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CluesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KilledDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_killed(self, id):
        try:
            return Killed.objects.get(id=id)
        except Killed.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        killed = self.get_killed(id)
        serializer = KilledSerializer(killed)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        killed = self.get_killed(id)
        serializer = KilledSerializer(killed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        killed = self.get_killed(id)
        killed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class KilledList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        killed = Killed.objects.all()
        serializer = KilledSerializer(killed, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KilledSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrisonersDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_prisoners(self, id):
        try:
            return Prisoners.objects.get(id=id)
        except Prisoners.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        prisoners = self.get_prisoners(id)
        serializer = PrisonersSerializer(prisoners)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        prisoners = self.get_prisoners(id)
        serializer = PrisonersSerializer(prisoners, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        prisoners = self.get_prisoners(id)
        prisoners.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PrisonersList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        prisoners = Prisoners.objects.all()
        serializer = PrisonersSerializer(prisoners, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PrisonersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_quest(self, id):
        try:
            return Quest.objects.get(id=id)
        except Quest.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        quest = self.quest(id)
        serializer = QuestSerializer(quest)
        return Response(serializer.data)


class DetectiveDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_detectives(self, id):
        try:
            return Detective.objects.get(id=id)
        except Detective.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        detective = self.get_detectives(id)
        serializer = DetectiveSerializer(detective)
        return Response(serializer.data)


class MercenariesDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_mercenaries(self, id):
        try:
            return Mercenaries.objects.get(id=id)
        except Mercenaries.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        mercenaries = self.get_mercenaries(id)
        serializer = MercenariesSerializer(mercenaries)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        mercenaries = self.get_mercenaries(id)
        serializer = MercenariesSerializer(mercenaries, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Mercenaries = self.get_mercenaries(id)
        Mercenaries.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MercenariesList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        mercenaries = Mercenaries.objects.all()
        serializer = MercenariesSerializer(mercenaries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MercenariesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SuspectDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_suspect(self, id):
        try:
            return Suspect.objects.get(id=id)
        except Suspect.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        suspect = self.get_suspect(id)
        serializer = SuspectSerializer(suspect)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        suspect = self.get_suspect(id)
        serializer = SuspectSerializer(suspect, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        suspect = self.get_suspect(id)
        suspect.delete()
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
