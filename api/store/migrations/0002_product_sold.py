# Generated by Django 4.2.4 on 2024-01-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.IntegerField(default=0),
        ),
    ]