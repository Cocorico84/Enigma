from game.models import Victim,Suspect
from game.serializers import VictimSerializer, SuspectSerializer
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
