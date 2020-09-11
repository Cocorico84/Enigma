from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Enigma.game.models import Victim
from Enigma.game.serializers import VictimSerializer

'''
Old version of the views
'''

@api_view(['GET', 'POST'])
def Victim_list(request):
    """
    List all code Victims, or create a new Victim.
    """
    if request.method == 'GET':
        victims = Victim.objects.all()
        serializer = VictimSerializer(victims, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VictimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Victim_detail(request, id):
    """
    Retrieve, update or delete a code Victim.
    """
    try:
        victim = Victim.objects.get(id=id)
    except Victim.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VictimSerializer(victim)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VictimSerializer(victim, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        victim.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)