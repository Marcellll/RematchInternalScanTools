from django.contrib import admin
from .models import Lot, Article, OrdreFabrication, PeseeProduction, Rerun

class LotAdmin(admin.ModelAdmin):
    list_display = ('lot', 'description')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('numero_article', 'description_article')

class PeseeProductionAdmin(admin.ModelAdmin):
    list_display = ('numero_pesee', 'status', 'poids')

class RerunAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_rerun', 'heure_rerun')

admin.site.register(Lot, LotAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(OrdreFabrication)
admin.site.register(PeseeProduction, PeseeProductionAdmin)
admin.site.register(Rerun, RerunAdmin)
