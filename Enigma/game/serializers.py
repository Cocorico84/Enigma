from rest_framework import serializers

from .models import Suspect, Detective, Quest, Prisoners, Killed, Insurance, Crime_location, Record, \
    Victim, \
    Mercenaries, Clues, Crime_details


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Insurance` instance, given the validated data.
        """
        return Insurance.objects.create(**validated_data)

    def update(self, Quest, validated_data):
        Insurance.id = validated_data.get('id', Insurance.id)
        Insurance.victim_insurance = validated_data.get('victim_insurance', Insurance.victim_insurance)
        Insurance.value = validated_data.get('value', Insurance.value)
        Insurance.save()
        return Insurance


class CluesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clues
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Clues` instance, given the validated data.
        """
        return Clues.objects.create(**validated_data)

    def update(self, Quest, validated_data):
        Clues.id = validated_data.get('id', Clues.id)
        Clues.clue = validated_data.get('clue', Clues.clue)
        Clues.crime_clues = validated_data.get('crime_clues', Clues.crime_clues)
        Clues.save()
        return Clues


class Crime_locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crime_location
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Crime_location` instance, given the validated data.
        """
        return Crime_location.objects.create(**validated_data)

    def update(self, Quest, validated_data):
        Crime_location.id = validated_data.get('id', Crime_location.id)
        Crime_location.crime = validated_data.get('crime', Crime_location.crime)
        Crime_location.location = validated_data.get('location', Crime_location.location)
        Crime_location.save()
        return Crime_location


class Crime_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crime_details
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Crime_details` instance, given the validated data.
        """
        return Crime_details.objects.create(**validated_data)

    def update(self, Quest, validated_data):
        Crime_details.id = validated_data.get('id', Crime_details.id)
        Crime_details.crime_quest = validated_data.get('crime_quest', Crime_details.crime_quest)
        Crime_details.victim_id = validated_data.get('antecedent', Crime_details.victim_id)
        Crime_details.estimated_date = validated_data.get('estimated_date', Crime_details.estimated_date)
        Crime_details.nature = validated_data.get('nature', Crime_details.nature)
        Crime_details.autopsia = validated_data.get('autopsia', Crime_details.autopsia)
        Crime_details.save()
        return Crime_details


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Record` instance, given the validated data.
        """
        return Prisoners.objects.create(**validated_data)

    def update(self, Quest, validated_data):
        Record.id = validated_data.get('id', Record.id)
        Record.suspect_id = validated_data.get('suspect_id', Record.suspect_id)
        Record.antecedent = validated_data.get('antecedent', Record.antecedent)
        Record.save()
        return Record


class PrisonersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prisoners
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Prisoners` instance, given the validated data.
        """
        return Prisoners.objects.create(**validated_data)

    def update(self, Quest, validated_data):
        Prisoners.id = validated_data.get('id', Quest.id)
        Prisoners.prisoner_id = validated_data.get('suspect_id', Prisoners.prisoner_id)
        Prisoners.prime_value = validated_data.get('prime_value', Prisoners.prime_value)
        Prisoners.save()
        return Prisoners


class KilledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Killed
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Killed` instance, given the validated data.
        """
        return Killed.objects.create(**validated_data)

    def update(self, Quest, validated_data):
        Killed.id = validated_data.get('id', Quest.id)
        Killed.murdered_id_id = validated_data.get('suspect_id', Killed.murdered_id)
        Killed.prime_value = validated_data.get('prime_value', Prisoners.prime_value)
        Killed.save()
        return Killed


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Quest` instance, given the validated data.
        """
        return Quest.objects.create(**validated_data)

    def update(self, Quest, validated_data):
        Quest.id = validated_data.get('id', Quest.id)
        Quest.title = validated_data.get('title', Quest.id)
        Quest.save()
        return Quest


class DetectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detective
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Detective` instance, given the validated data.
        """
        return Detective.objects.create(**validated_data)

    def update(self, Detective, validated_data):
        Detective.id = validated_data.get('id', Detective.id)
        Detective.cover = validated_data.get('cover', Detective.cover)
        Detective.money = validated_data.get('money', Detective.money)
        Detective.number_of_mercenaries = validated_data.get('number_of_mercenaries', Detective.number_of_mercenaries)
        Detective.save()
        return Detective


class MercenariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercenaries
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Mercenaries` instance, given the validated data.
        """
        return Mercenaries.objects.create(**validated_data)

    def update(self, Mercenaries, validated_data):
        Mercenaries.id = validated_data.get('id', Mercenaries.id)
        Mercenaries.first_name = validated_data.get('first_name', Mercenaries.first_name)
        Mercenaries.last_name = validated_data.get('last_name', Mercenaries.last_name)
        Mercenaries.age = validated_data.get('age', Mercenaries.age)
        Mercenaries.gender = validated_data.get('gender', Mercenaries.gender)
        Mercenaries.cost = validated_data.get('cost', Mercenaries.cost)
        Mercenaries.number_of_actions = validated_data('number_of_actions', Mercenaries.number_of_actions)
        Mercenaries.save()
        return Mercenaries


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
        Create and return a new `Victim` instance, given the validated data.
        """
        return Victim.objects.create(**validated_data)

    def update(self, Victim, validated_data):
        """
        Update and return an existing `Victim` instance, given the validated data.
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
