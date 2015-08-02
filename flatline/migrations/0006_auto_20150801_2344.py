# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatline', '0005_auto_20150801_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='end',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='start',
            field=models.DateField(null=True, blank=True),
        ),
    ]
