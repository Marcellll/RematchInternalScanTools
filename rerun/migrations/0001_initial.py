# Generated by Django 5.1.7 on 2025-03-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('numero_article', models.BigIntegerField(db_column='Numero_article')),
                ('description_article', models.TextField(db_column='Description_article')),
                ('front_back', models.TextField(blank=True, db_column='Front/Back', null=True)),
                ('nomenclature', models.BigIntegerField(blank=True, db_column='Nomenclature', null=True)),
                ('categorie', models.TextField(blank=True, db_column='Categorie', null=True)),
            ],
            options={
                'db_table': 'Article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('lot', models.BigIntegerField(blank=True, db_column='Lot', null=True)),
                ('date_modification', models.DateField(blank=True, db_column='Date_modification', null=True)),
                ('heure_modification', models.TimeField(blank=True, db_column='Heure_modification', null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
            ],
            options={
                'db_table': 'Lot',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdreFabrication',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('date_debut', models.DateField(blank=True, db_column='Date_debut', null=True)),
                ('date_fin', models.DateField(blank=True, db_column='Date_fin', null=True)),
                ('status_of', models.TextField(blank=True, db_column='Status_OF', null=True)),
            ],
            options={
                'db_table': 'Ordre_fabrication',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PeseeProduction',
            fields=[
                ('poids', models.DecimalField(blank=True, db_column='Poids', decimal_places=65535, max_digits=65535, null=True)),
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('date_creation', models.DateField(blank=True, db_column='Date_creation', null=True)),
                ('heure_creation', models.TimeField(blank=True, db_column='Heure_creation', null=True)),
                ('numero_pesee', models.BigIntegerField(blank=True, db_column='Numero_pesee', null=True)),
                ('status', models.TextField(blank=True, db_column='Status', null=True)),
            ],
            options={
                'db_table': 'Pesee_production',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rerun',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('date_rerun', models.DateField(auto_now_add=True, db_column='Date_rerun', null=True)),
                ('heure_rerun', models.TimeField(auto_now_add=True, db_column='Heure_rerun', null=True)),
            ],
            options={
                'db_table': 'Rerun',
                'ordering': ['-date_rerun', '-heure_rerun'],
                'managed': False,
            },
        ),
    ]
