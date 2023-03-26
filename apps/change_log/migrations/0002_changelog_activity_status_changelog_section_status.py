# Generated by Django 4.0.5 on 2023-03-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='changelog',
            name='activity_status',
            field=models.CharField(choices=[('Other', 'Other'), ('Update', 'Update'), ('Delete', 'Not Delete')], default='Other', max_length=50),
        ),
        migrations.AddField(
            model_name='changelog',
            name='section_status',
            field=models.CharField(choices=[('Other', 'Other'), ('Book', 'Book'), ('Author', 'Author'), ('RentHistory', 'Rent History'), ('TaskLibrarian', 'Task Librarian'), ('TaskLibrarianDetail', 'TaskLibrarian Detail'), ('TaskReport', 'Task Report')], default='Other', max_length=50),
        ),
    ]
