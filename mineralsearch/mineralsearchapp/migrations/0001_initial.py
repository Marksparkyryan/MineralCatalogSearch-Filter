# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('image_filename', models.CharField(max_length=256)),
                ('image_caption', models.CharField(max_length=256)),
                ('category', models.CharField(max_length=256)),
                ('formula', models.CharField(max_length=256)),
                ('strunz_classification', models.CharField(max_length=256)),
                ('crystal_system', models.CharField(max_length=256)),
                ('unit_cell', models.TextField(max_length=528)),
                ('color', models.CharField(max_length=256)),
                ('crystal_symmetry', models.CharField(max_length=256)),
                ('cleavage', models.CharField(max_length=256)),
                ('mohs_scale_hardness', models.CharField(max_length=256)),
                ('luster', models.CharField(max_length=256)),
                ('streak', models.CharField(max_length=256)),
                ('diaphaneity', models.CharField(max_length=256)),
                ('group', models.CharField(max_length=256)),
                ('optical_properties', models.CharField(max_length=256)),
                ('refractive_index', models.CharField(max_length=256)),
                ('crystal_habit', models.CharField(max_length=256)),
                ('specific_gravity', models.CharField(max_length=256)),
            ],
        ),
    ]
