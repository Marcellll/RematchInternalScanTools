from django.db import models
from article.models import Article
from production_management.models import OrdreFabrication

class PeseeProduction(models.Model):
    id_ordre_fabrication = models.ForeignKey(OrdreFabrication, models.DO_NOTHING, db_column='ID_ordre_fabrication', blank=True, null=True)  # Field name made lowercase.
    poids = models.DecimalField(db_column='Poids', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='ID_article', blank=True, null=True)  # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date_creation = models.DateField(db_column='Date_creation', blank=True, null=True)  # Field name made lowercase.
    heure_creation = models.TimeField(db_column='Heure_creation', blank=True, null=True)  # Field name made lowercase.
    numero_pesee = models.BigIntegerField(db_column='Numero_pesee', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.numero_pesee}"

    class Meta:
        managed = False
        db_table = 'Pesee_production'

class Rerun(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pesee_production = models.ForeignKey(PeseeProduction, models.DO_NOTHING, db_column='ID_Pesee_production', blank=True, null=True)  # Field name made lowercase.
    id_ordre_fabrication_rerun = models.ForeignKey(OrdreFabrication, models.DO_NOTHING, db_column='ID_Ordre_fabrication_rerun', blank=True, null=True)  # Field name made lowercase.
    date_rerun = models.DateField(db_column='Date_rerun', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    heure_rerun = models.TimeField(db_column='Heure_rerun', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rerun'
        ordering = ['-date_rerun', '-heure_rerun']
    
    def __str__(self):
        return f"{self.id}"


