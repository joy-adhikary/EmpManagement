# Generated by Django 4.2.7 on 2024-01-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=60)),
                ('user_type', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
