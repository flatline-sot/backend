# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatline', '0004_auto_20150801_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='flat',
            field=models.ForeignKey(blank=True, to='flatline.Flat', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='flat',
            field=models.ForeignKey(blank=True, to='flatline.Flat', null=True),
        ),
    ]
