# Generated by Django 4.2.3 on 2023-07-24 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='nbrmatier',
            field=models.CharField(max_length=250),
        ),
    ]
