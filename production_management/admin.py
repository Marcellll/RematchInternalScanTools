from django.contrib import admin
from .models import OrdreFabrication, ArticleParLot

class OrdreFabricationAdmin(admin.ModelAdmin):
    list_display = ('id_lot__lot', 'status_of')
    list_select_related = ('id_lot',)

admin.site.register(OrdreFabrication, OrdreFabricationAdmin)
admin.site.register(ArticleParLot)
