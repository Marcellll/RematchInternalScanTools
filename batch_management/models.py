from django.db import models

from article.models import Article, FrontBack

        
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


