# Generated by Django 4.0.4 on 2022-05-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_event_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='added_by',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]