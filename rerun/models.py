from django.db import models

class Article(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero_article = models.BigIntegerField(db_column='Numero_article')  # Field name made lowercase.
    description_article = models.TextField(db_column='Description_article')  # Field name made lowercase.
    front_back = models.TextField(db_column='Front/Back', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nomenclature = models.BigIntegerField(db_column='Nomenclature', blank=True, null=True)  # Field name made lowercase.
    categorie = models.TextField(db_column='Categorie', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.description_article

    class Meta:
        managed = False
        db_table = 'Article'

class Lot(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='ID_Article', blank=True, null=True)  # Field name made lowercase.
    lot = models.BigIntegerField(db_column='Lot', blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateField(db_column='Date_modification', blank=True, null=True)  # Field name made lowercase.
    heure_modification = models.TimeField(db_column='Heure_modification', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.lot} : {self.description}"
    
    class Meta:
        managed = False
        db_table = 'Lot'

class OrdreFabrication(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_lot = models.ForeignKey(Lot, models.DO_NOTHING, db_column='ID_Lot', blank=True, null=True)  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_debut', blank=True, null=True)  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_fin', blank=True, null=True)  # Field name made lowercase.
    status_of = models.TextField(db_column='Status_OF', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.id}"

    class Meta:
        managed = False
        db_table = 'Ordre_fabrication'

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


