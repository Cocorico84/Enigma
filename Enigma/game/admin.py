from django.contrib import admin
from .models import Suspect, Insurance, Crime_details, Record, Victim, Quest

admin.site.register(Quest)
admin.site.register(Victim)
admin.site.register(Record)
admin.site.register(Crime_details)
admin.site.register(Insurance)
admin.site.register(Suspect)
# Register your models here.

