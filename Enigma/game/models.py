from django.db import models

"""
linux shell delete commands
rm -f path/db.sqlite3
rm -f path/migrations/migration_file
windows shell delete commands
del path/db.sqlite3
del path/migrations/migration_file
"""


# Create your models here.

class Quest(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    title = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.id + ' ' + self.title


class Victim(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    first_name = models.CharField(max_length=30, default=None)
    last_name = models.CharField(max_length=30, default=None)
    autopsia = models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=10, default=None)
    age = models.IntegerField(default=None)
    ethnic_group = models.CharField(max_length=15, default=None)
    height = models.IntegerField(default=None)
    hair_color = models.CharField(max_length=15, default=None)
    eye_color = models.CharField(max_length=15, default=None)
    profession = models.CharField(max_length=30, default=None)
    resident = models.CharField(max_length=30, default=None)
    income = models.IntegerField(default=None)
    insurance_owner = models.BooleanField(default=None)

    def __str__(self):
        return self.id + self.first_name + self.last_name + self.autopsia + self.gender + self.age + self.ethnic_group + self.height + self.hair_color + self.eye_color + self.profession + self.resident + self.income + self.insurance_owner

    class Meta:
        ordering = ["id"]


class Insurance(models.Model):
    victim_insurance = models.ForeignKey(Victim, default=None, on_delete=models.CASCADE)
    value = models.IntegerField(default=None)

    def __str__(self):
        return self.value + self.victim_insurance


class Suspect(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    first_name = models.CharField(max_length=30, default=None)
    last_name = models.CharField(max_length=30, default=None)
    gender = models.CharField(max_length=10, default=None)
    age = models.IntegerField(default=None)
    ethnic_group = models.CharField(max_length=15, default=None)
    height = models.IntegerField(default=None)
    hair_color = models.CharField(max_length=15, default=None)
    eye_color = models.CharField(max_length=15, default=None)
    profession = models.CharField(max_length=30, default=None)
    resident = models.CharField(max_length=30, default=None)
    income = models.IntegerField(default=None)
    bound_with_victim = models.ForeignKey(Victim, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.id + self.first_name + ' ' + self.last_name + self.gender + self.age + self.ethnic_group + self.height + self.hair_color + self.eye_color + self.profession + self.resident + self.bound_with_victim

    class Meta:
        ordering = ['id']


class Investigation(models.Model):
    examination = models.ForeignKey(Suspect, default=None, on_delete=models.CASCADE)
    Question1 = models.CharField(max_length=500, default=None)
    Response1 = models.CharField(max_length=500, default=None)
    Question2 = models.CharField(max_length=500, default=None)
    Response2 = models.CharField(max_length=500, default=None)
    Question3 = models.CharField(max_length=500, default=None)
    Response3 = models.CharField(max_length=500, default=None)
    Question4 = models.CharField(max_length=500, default=None)
    Response4 = models.CharField(max_length=500, default=None)
    Question5 = models.CharField(max_length=500, default=None)
    Response5 = models.CharField(max_length=500, default=None)
    Question6 = models.CharField(max_length=500, default=None)
    Response6 = models.CharField(max_length=500, default=None)

    def __str__(self):
        return self.examination


class Record(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    suspect_id = models.ForeignKey(Suspect, default=None, on_delete=models.CASCADE)
    antecedent = models.CharField(max_length=100, default=None)
    investigation = models.ForeignKey(Investigation, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.id + self.suspect_id + self.antecedent + self.investigation


class Crime_detail(models.Model):
    crime_id = models.IntegerField(primary_key=True, default=None)
    quest_id = models.ForeignKey(Quest, default=None, on_delete=models.CASCADE)
    victim_id = models.ForeignKey(Victim, default=None, on_delete=models.CASCADE)
    estimated_date = models.IntegerField(default=None)
    nature = models.CharField(max_length=30, default=None)
    weapon_used = models.CharField(max_length=30, default=None)
    autopsia = models.CharField(max_length=100, default=None)
    optional_clues = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.crime_id + self.quest_id + self.victim_id + self.estimated_date + self.nature + self.weapon_used + self.autopsia + self.optional_clues


class Crime_location(models.Model):
    crime = models.ForeignKey(Crime_detail, default=None, on_delete=models.CASCADE)
    country = models.CharField(max_length=30, default=None)
    town = models.CharField(max_length=30, default=None)
    house = models.CharField(max_length=30, default=None)
    room = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.crime + self.country + self.town + self.house + self.room
