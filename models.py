# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero_article = models.BigIntegerField(db_column='Numero_article')  # Field name made lowercase.
    description_article = models.TextField(db_column='Description_article')  # Field name made lowercase.
    front_back = models.TextField(db_column='Front/Back', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nomenclature = models.BigIntegerField(db_column='Nomenclature', blank=True, null=True)  # Field name made lowercase.
    categorie = models.TextField(db_column='Categorie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Article'


class ArticleParLot(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_lot = models.ForeignKey('Lot', models.DO_NOTHING, db_column='ID_Lot', blank=True, null=True)  # Field name made lowercase.
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='ID_Article', blank=True, null=True)  # Field name made lowercase.
    date_creation = models.DateField(db_column='Date_creation', blank=True, null=True)  # Field name made lowercase.
    heure_creation = models.TimeField(db_column='Heure_creation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Article_par_lot'


class Camion(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date_entree = models.DateField(db_column='Date_entree', blank=True, null=True)  # Field name made lowercase.
    heure_entree = models.TimeField(db_column='Heure_entree', blank=True, null=True)  # Field name made lowercase.
    date_sortie = models.DateField(db_column='Date_sortie', blank=True, null=True)  # Field name made lowercase.
    heure_sortie = models.TimeField(db_column='Heure_sortie', blank=True, null=True)  # Field name made lowercase.
    poids_in = models.BigIntegerField(db_column='Poids_in', blank=True, null=True)  # Field name made lowercase.
    poids_out = models.BigIntegerField(db_column='Poids_out', blank=True, null=True)  # Field name made lowercase.
    id_chargement = models.ForeignKey('Chargement', models.DO_NOTHING, db_column='ID_Chargement', blank=True, null=True)  # Field name made lowercase.
    poids_net = models.BigIntegerField(db_column='Poids_net', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    numero_interne = models.BigIntegerField(db_column='Numero_interne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Camion'


class Chargement(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_debut', blank=True, null=True)  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_fin', blank=True, null=True)  # Field name made lowercase.
    id_lot = models.BigIntegerField(db_column='ID_Lot', blank=True, null=True)  # Field name made lowercase.
    numero_chargement = models.BigIntegerField(db_column='Numero_chargement', blank=True, null=True)  # Field name made lowercase.
    chargement_dechargement = models.TextField(db_column='Chargement/Dechargement', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    client = models.TextField(db_column='Client', blank=True, null=True)  # Field name made lowercase.
    adresse_livraison = models.TextField(db_column='Adresse livraison', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chargement'


class Inventaire(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pesee = models.BigIntegerField(db_column='ID_Pesee', blank=True, null=True)  # Field name made lowercase.
    emplacement = models.TextField(db_column='Emplacement', blank=True, null=True)  # Field name made lowercase.
    qualitÚ = models.TextField(db_column='QualitÚ', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    id_camion = models.BigIntegerField(db_column='ID_Camion', blank=True, null=True)  # Field name made lowercase.
    date_deplacement = models.DateField(db_column='Date_deplacement', blank=True, null=True)  # Field name made lowercase.
    heure_deplacement = models.TimeField(db_column='Heure_deplacement', blank=True, null=True)  # Field name made lowercase.
    initiale_deplacement = models.TextField(db_column='Initiale_deplacement', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inventaire'


class Lot(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='ID_Article', blank=True, null=True)  # Field name made lowercase.
    lot = models.BigIntegerField(db_column='Lot', blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateField(db_column='Date_modification', blank=True, null=True)  # Field name made lowercase.
    heure_modification = models.TimeField(db_column='Heure_modification', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lot'


class Nomenclature(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='ID_Article', blank=True, null=True)  # Field name made lowercase.
    id_nomenclature = models.BigIntegerField(db_column='ID_Nomenclature', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nomenclature'


class OrdreFabrication(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_lot = models.ForeignKey(Lot, models.DO_NOTHING, db_column='ID_Lot', blank=True, null=True)  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_debut', blank=True, null=True)  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_fin', blank=True, null=True)  # Field name made lowercase.
    status_of = models.TextField(db_column='Status_OF', blank=True, null=True)  # Field name made lowercase.

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

    class Meta:
        managed = False
        db_table = 'Pesee_production'


class QuantiteALivrer(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_chargement = models.BigIntegerField(db_column='ID_Chargement', blank=True, null=True)  # Field name made lowercase.
    qualitÚ = models.TextField(db_column='QualitÚ', blank=True, null=True)  # Field name made lowercase.
    id_lot = models.BigIntegerField(db_column='ID_Lot', blank=True, null=True)  # Field name made lowercase.
    quantitÚ = models.BigIntegerField(db_column='QuantitÚ', blank=True, null=True)  # Field name made lowercase.
    id_article = models.BigIntegerField(db_column='ID_Article', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Quantite_a_livrer'


class Rerun(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pesee_production = models.ForeignKey(PeseeProduction, models.DO_NOTHING, db_column='ID_Pesee_production', blank=True, null=True)  # Field name made lowercase.
    id_ordre_fabrication_rerun = models.ForeignKey(OrdreFabrication, models.DO_NOTHING, db_column='ID_Ordre_fabrication_rerun', blank=True, null=True)  # Field name made lowercase.
    date_rerun = models.DateField(db_column='Date_rerun', blank=True, null=True)  # Field name made lowercase.
    heure_rerun = models.TimeField(db_column='Heure_rerun', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rerun'


class Scan(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_camion = models.BigIntegerField(db_column='ID_Camion', blank=True, null=True)  # Field name made lowercase.
    id_pesee = models.BigIntegerField(db_column='ID_pesee', blank=True, null=True)  # Field name made lowercase.
    date_scan = models.DateField(db_column='Date_scan', blank=True, null=True)  # Field name made lowercase.
    heure_scan = models.TimeField(db_column='Heure_scan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Scan'


class AccountsCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accounts_customuser'


class AccountsCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_customuser_groups'
        unique_together = (('customuser', 'group'),)


class AccountsCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
