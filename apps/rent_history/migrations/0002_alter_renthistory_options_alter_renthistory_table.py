# Generated by Django 4.0.5 on 2023-03-26 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent_history', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='renthistory',
            options={'verbose_name': 'Rent History'},
        ),
        migrations.AlterModelTable(
            name='renthistory',
            table='rent_history',
        ),
    ]
