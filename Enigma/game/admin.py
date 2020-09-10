from django.contrib import admin
from .models import Suspect, Insurance, Crime_location, Crime_detail, Record, Investigation, Victim, Quest

admin.site.register(Quest)
admin.site.register(Victim)
admin.site.register(Record)
admin.site.register(Investigation)
admin.site.register(Crime_detail)
admin.site.register(Crime_location)
admin.site.register(Insurance)
admin.site.register(Suspect)
# Register your models here.

