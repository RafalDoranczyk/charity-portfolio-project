# Generated by Django 3.0.5 on 2020-04-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0003_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]