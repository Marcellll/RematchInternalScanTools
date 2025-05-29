from django.db import models
from enum import Enum

class FrontBack(Enum):
    Frontend = "Front end"
    Backend = "Back end"

class Article(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero_article = models.BigIntegerField(db_column='Numero_article')  # Field name made lowercase.
    description_article = models.TextField(db_column='Description_article')  # Field name made lowercase.
    front_back = models.TextField(db_column='Front/Back', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    categorie = models.TextField(db_column='Categorie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Article'
        ordering = ['numero_article']

    def __str__(self):
        return f"{self.numero_article} - {self.description_article}"
    
class Nomenclature(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_article = models.ForeignKey(Article, models.DO_NOTHING, related_name='article_a_nomenclature', db_column='ID_Article', blank=True, null=True)  # Field name made lowercase.
    id_nomenclature = models.ForeignKey(Article, models.DO_NOTHING, related_name='article_de_nomenclature', db_column='ID_Nomenclature', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nomenclature'
        ordering = ['id_article__numero_article']

    def __str__(self):
        return f"{self.id_article.description_article} - {self.id_nomenclature.description_article}"