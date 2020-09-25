from game.models import Victim, Suspect, Mercenaries, Prisoners, Killed, Clues, Crime_details, Record, \
    Insurance
from game.serializers import VictimSerializer, SuspectSerializer, MercenariesSerializer, PrisonersSerializer, \
    KilledSerializer, CluesSerializer, Crime_detailsSerializer, \
    RecordSerializer, InsuranceSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


class VictimList(ListAPIView):
    queryset = Victim.objects.all()
    serializer_class = VictimSerializer
    filter_backends = (SearchFilter, OrderingFilter)


class SuspectList(ListAPIView):
    queryset = Suspect.objects.all()
    serializer_class = SuspectSerializer
    filter_backends = (SearchFilter, OrderingFilter)


class MercenariesList(ListAPIView):
    queryset = Mercenaries.objects.all()
    serializer_class = MercenariesSerializer
    filter_backends = (SearchFilter, OrderingFilter)


class PrisonersList(ListAPIView):
    queryset = Prisoners.objects.all()
    serializer_class = PrisonersSerializer
    filter_backends = (SearchFilter, OrderingFilter)


class KilledList(ListAPIView):
    queryset = Killed.objects.all()
    serializer_class = KilledSerializer
    filter_backends = (SearchFilter, OrderingFilter)


class CluesList(ListAPIView):
    queryset = Clues.objects.all()
    serializer_class = CluesSerializer
    filter_backends = (SearchFilter, OrderingFilter)


class Crime_detailsList(ListAPIView):
    queryset = Crime_details.objects.all()
    serializer_class = Crime_detailsSerializer
    filter_backends = (SearchFilter, OrderingFilter)


# class Crime_locationList(ListAPIView):
#     queryset = Crime_location.objects.all()
#     serializer_class = Crime_locationSerializer
#     filter_backends = (SearchFilter, OrderingFilter)


class RecordList(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = (SearchFilter, OrderingFilter)


class InsuranceList(ListAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    filter_backends = (SearchFilter, OrderingFilter)
