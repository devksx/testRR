# Generated by Django 3.1.7 on 2021-04-01 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importdata', '0002_zipprofilefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersfile',
            name='csvFile',
            field=models.FileField(upload_to='teacherCSV/'),
        ),
        migrations.AlterField(
            model_name='zipprofilefile',
            name='zipFile',
            field=models.FileField(upload_to='pics/'),
        ),
    ]