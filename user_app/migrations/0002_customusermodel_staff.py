# Generated by Django 4.0.4 on 2022-05-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]