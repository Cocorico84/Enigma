from rest_framework import serializers
from .models import Suspect, Record

class SuspectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suspect
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'