# Generated by Django 4.2 on 2023-04-30 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aitools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templateai',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]