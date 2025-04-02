from django.db import models
from enum import Enum

class FrontBack(Enum):
    Frontend = "Front end"
    Backend = "Back end"

class StatusOF(Enum):
    CREE= "Crée"
    PLANIFIE = "Planifié"
    TERMINE = "Terminé"

class Article(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero_article = models.BigIntegerField(db_column='Numero_article')  # Field name made lowercase.
    description_article = models.TextField(db_column='Description_article')  # Field name made lowercase.
    front_back = models.TextField(db_column='Front/Back', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    categorie = models.TextField(db_column='Categorie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Article'
    
    def __str__(self):
        return f"{self.numero_article} - {self.description_article}"
        
class Lot(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='ID_Article', blank=True, null=True)  # Field name made lowercase.
    lot = models.BigIntegerField(db_column='Lot', blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateField(db_column='Date_modification', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    heure_modification = models.TimeField(db_column='Heure_modification', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lot'

    def __str__(self):
        return f"{self.lot} - {self.description}"
    
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
    
class Nomenclature(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_article = models.ForeignKey(Article, models.DO_NOTHING, related_name='article_a_nomenclature', db_column='ID_Article', blank=True, null=True)  # Field name made lowercase.
    id_nomenclature = models.ForeignKey(Article, models.DO_NOTHING, related_name='article_de_nomenclature', db_column='ID_Nomenclature', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nomenclature'

    def __str__(self):
        return f"{self.id_article.description_article} - {self.id_nomenclature.description_article}"
    

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

