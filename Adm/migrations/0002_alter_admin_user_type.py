# Generated by Django 4.2.7 on 2024-02-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='user_type',
            field=models.CharField(max_length=20),
        ),
    ]
