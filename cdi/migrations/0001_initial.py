# Generated by Django 4.2.3 on 2023-07-24 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('matiere1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matiere1_formations', to='cdi.matiere')),
                ('matiere2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matiere2_formations', to='cdi.matiere')),
                ('matiere3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matiere3_formations', to='cdi.matiere')),
                ('matiere4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matiere4_formations', to='cdi.matiere')),
                ('matiere5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matiere5_formations', to='cdi.matiere')),
                ('nbrmatier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nbrmatier_formations', to='cdi.matiere')),
            ],
        ),
    ]