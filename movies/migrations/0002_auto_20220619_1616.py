# Generated by Django 3.2.7 on 2022-06-19 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Film', 'verbose_name_plural': 'Films'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.AddField(
            model_name='movie',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='describe',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(20)], verbose_name='Describe'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]
