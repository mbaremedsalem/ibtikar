# Generated by Django 4.2.3 on 2023-08-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdi', '0004_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='pourcatange',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
