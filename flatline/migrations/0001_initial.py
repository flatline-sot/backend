# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('cost', models.DecimalField(max_digits=6, decimal_places=2)),
                ('cost_per_user', models.DecimalField(max_digits=6, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('powershop_user', models.CharField(max_length=256)),
                ('powershop_password', models.CharField(max_length=50)),
                ('numberOfMembers', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('flat', models.OneToOneField(default=0, to='flatline.Flat')),
            ],
        ),
        migrations.CreateModel(
            name='UserBill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_paid', models.DateField()),
                ('bill', models.ForeignKey(to='flatline.Bill')),
                ('user', models.ForeignKey(to='flatline.User')),
            ],
        ),
    ]
