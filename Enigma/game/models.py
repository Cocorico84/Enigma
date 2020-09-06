from django.db import models

# Create your models here.
class Suspect(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Record(models.Model):
    suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE)
    antecedent = models.CharField(max_length=100)


