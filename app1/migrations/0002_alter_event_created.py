# Generated by Django 4.0.4 on 2022-05-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.CharField(max_length=100),
        ),
    ]
