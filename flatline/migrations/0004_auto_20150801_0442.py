# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatline', '0003_auto_20150801_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='oauth_token',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='oauth_token_secret',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
    ]
