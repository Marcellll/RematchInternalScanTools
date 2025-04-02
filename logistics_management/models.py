from django.db import models
from enum import Enum
from batch_management.models import Lot

class ChargementDechargement(Enum):
    CHARGEMENT = "Chargement"
    DECHARGEMENT = "Dechargement"

class ChargementStatus(Enum):
    OUVERT = "Ouvert"
    TERMINE = "Terminé"

class Chargement(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_debut', blank=True, null=True)  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_fin', blank=True, null=True)  # Field name made lowercase.
    id_lot = models.ForeignKey(Lot, models.DO_NOTHING, db_column='ID_Lot', blank=True, null=True)  # Field name made lowercase.
    numero_chargement = models.BigIntegerField(db_column='Numero_chargement', blank=True, null=True)  # Field name made lowercase.
    chargement_dechargement = models.TextField(db_column='Chargement/Dechargement', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    client = models.TextField(db_column='Client', blank=True, null=True)  # Field name made lowercase.
    adresse_livraison = models.TextField(db_column='Adresse livraison', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chargement'

    def __str__(self):
        return f"{self.numero_chargement}"
    
class Camion(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date_entree = models.DateField(db_column='Date_entree', blank=True, null=True)  # Field name made lowercase.
    heure_entree = models.TimeField(db_column='Heure_entree', blank=True, null=True)  # Field name made lowercase.
    date_sortie = models.DateField(db_column='Date_sortie', blank=True, null=True)  # Field name made lowercase.
    heure_sortie = models.TimeField(db_column='Heure_sortie', blank=True, null=True)  # Field name made lowercase.
    poids_in = models.BigIntegerField(db_column='Poids_in', blank=True, null=True)  # Field name made lowercase.
    poids_out = models.BigIntegerField(db_column='Poids_out', blank=True, null=True)  # Field name made lowercase.
    id_chargement = models.ForeignKey(Chargement, models.DO_NOTHING, db_column='ID_Chargement', blank=True, null=True)  # Field name made lowercase.
    poids_net = models.BigIntegerField(db_column='Poids_net', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    numero_interne = models.BigIntegerField(db_column='Numero_interne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Camion'

    def __str__(self):
        return f"{self.id_chargement.numero_chargement} - {self.description}"
    
