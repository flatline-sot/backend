# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatline', '0002_remove_user_flat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='powershop_password',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='powershop_user',
        ),
    ]
