# Generated by Django 4.2.7 on 2024-04-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkEmpWithAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=502)),
                ('position', models.CharField(default='', max_length=502)),
                ('salary', models.IntegerField()),
                ('emp_id', models.IntegerField()),
            ],
        ),
    ]
