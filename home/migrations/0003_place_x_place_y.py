# Generated by Django 4.1 on 2023-11-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_userchoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='x',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='y',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
