from django.contrib import admin
from .models import PeseeProduction, Rerun


class PeseeProductionAdmin(admin.ModelAdmin):
    list_display = ('numero_pesee', 'status', 'poids')

class RerunAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_rerun', 'heure_rerun')

admin.site.register(PeseeProduction, PeseeProductionAdmin)
admin.site.register(Rerun, RerunAdmin)
