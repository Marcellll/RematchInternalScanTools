from django.db import models
from enum import Enum

from article.models import Article, FrontBack, Nomenclature
from batch_management.models import Lot

class StatusOF(Enum):
    CREE= "Crée"
    PLANIFIE = "Planifié"
    TERMINE = "Terminé"

class OrdreFabrication(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_lot = models.ForeignKey(Lot, models.DO_NOTHING, db_column='ID_Lot', blank=True, null=True)  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_debut', blank=True, null=True)  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_fin', blank=True, null=True)  # Field name made lowercase.
    status_of = models.TextField(db_column='Status_OF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ordre_fabrication'
    
    def __str__(self):
        return f"{self.id} - {self.status_of}"
        

class ArticleParLot(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_ordre_fabrication = models.ForeignKey(OrdreFabrication, models.DO_NOTHING, db_column='ID_Ordre_fabrication', blank=True, null=True)  # Field name made lowercase.
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='ID_Article', blank=True, null=True)  # Field name made lowercase.
    date_creation = models.DateField(db_column='Date_creation', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    heure_creation = models.TimeField(db_column='Heure_creation', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Article_par_lot'

    def __str__(self):
        return f"{self.id_ordre_fabrication.id_lot.lot} - {self.id_article.description_article}"

