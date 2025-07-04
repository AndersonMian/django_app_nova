# Generated by Django 5.2.1 on 2025-05-15 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('type_client', models.CharField(choices=[('entreprise', 'Entreprise'), ('particulier', 'Particulier')], max_length=20)),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=20)),
                ('reference_client', models.CharField(max_length=50, unique=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ['nom'],
            },
        ),
    ]
