from django.contrib.auth.models import User
from rest_framework import serializers

from . import models
from .models import Suspect, Quest, Insurance, Crime_location, Crime_detail, Record, Investigation, Victim


class VictimSerializer(serializers.ModelSerializer):
    """

    Before sending data to client, serialization of data to json necessary
    """

    class Meta:
        model = Victim
        fields = '__all__'
        # fields = ['id', 'first_name', 'last_name', 'autopsia', 'gender', 'age', 'ethnic_group', 'height', 'hair_color',
        #           'eye_color', 'profession', 'resident', 'income', 'insurance_owner']

    def create(self, validated_data):
        """
        Create and return a new `Suspect` instance, given the validated data.
        """
        return Victim.objects.create(**validated_data)

    def update(self, Victim, validated_data):
        """
        Update and return an existing `Suspect` instance, given the validated data.
        """
        Victim.id = validated_data.get('id', Victim.id)
        Victim.first_name = validated_data.get('first_name', Victim.first_name)
        Victim.last_name = validated_data.get('last_name', Victim.last_name)
        Victim.autopsia = validated_data.get('autopsia', Victim.autopsia)
        Victim.gender = validated_data.get('gender', Victim.gender)
        Victim.age = validated_data.get('age', Victim.age)
        Victim.ethnic_group = validated_data.get('ethnic_group', Victim.ethnic_group)
        Victim.height = validated_data.get('height', Victim.height)
        Victim.hair_color = validated_data.get('hair_color', Victim.hair_color)
        Victim.eye_color = validated_data.get('eye_color', Victim.eye_color)
        Victim.profession = validated_data.get('profession', Victim.profession)
        Victim.resident = validated_data.get('resident', Victim.resident)
        Victim.income = validated_data.get('income', Victim.income)
        Victim.insurance_owner = validated_data.get('insurance_owner', Victim.insurance_owner)
        Victim.save()
        return Victim


class SuspectSerializer(serializers.ModelSerializer):
    """

    Before sending data to client, serialization of data to json necessary
    """

    class Meta:
        model = Suspect
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Suspect` instance, given the validated data.
        """
        return Suspect.objects.create(**validated_data)

    def update(self, Suspect, validated_data):
        """
        Update and return an existing `Suspect` instance, given the validated data.
        """
        Suspect.id = validated_data.get('id', Suspect.id)
        Suspect.first_name = validated_data.get('first_name', Suspect.first_name)
        Suspect.last_name = validated_data.get('last_name', Suspect.last_name)
        Suspect.gender = validated_data.get('gender', Suspect.gender)
        Suspect.age = validated_data.get('age', Suspect.age)
        Suspect.ethnic_group = validated_data.get('ethnic_group', Suspect.ethnic_group)
        Suspect.height = validated_data.get('height', Suspect.height)
        Suspect.hair_color = validated_data.get('hair_color', Suspect.hair_color)
        Suspect.eye_color = validated_data.get('eye_color', Suspect.eye_color)
        Suspect.profession = validated_data.get('profession', Suspect.profession)
        Suspect.resident = validated_data.get('resident', Suspect.resident)
        Suspect.income = validated_data.get('income', Suspect.income)
        Suspect.bound_with_victim = validated_data.get('bound_with_victim', Suspect.bound_with_victim)
        Suspect.save()
        return Suspect
