# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='posting_system',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ischildthread', models.NullBooleanField(default=False)),
                ('fromuser', models.CharField(max_length=300, null=True, blank=True)),
                ('touser', models.CharField(max_length=300, null=True, blank=True)),
                ('date', models.CharField(max_length=300, null=True, blank=True)),
                ('user_item', models.CharField(max_length=300, null=True, blank=True)),
                ('user', models.CharField(max_length=300, null=True, blank=True)),
                ('item', models.CharField(max_length=300, null=True, blank=True)),
                ('subject', models.CharField(max_length=300, null=True, blank=True)),
                ('message', models.CharField(max_length=300, null=True, blank=True)),
                ('bid_amount', models.CharField(max_length=300, null=True, blank=True)),
                ('thread', models.CharField(max_length=300, null=True, blank=True)),
                ('user_has', models.NullBooleanField(default=False)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2015, 4, 3, 1, 23, 44, 657397))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='postinglisting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=30, null=True, blank=True)),
                ('highest_price', models.DecimalField(max_length=30, null=True, max_digits=8, decimal_places=3, blank=True)),
                ('location', models.CharField(max_length=30, null=True, blank=True)),
                ('location_str', models.CharField(max_length=30, null=True, blank=True)),
                ('distance_from_location', models.DecimalField(max_length=30, null=True, max_digits=8, decimal_places=4, blank=True)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d', blank=True)),
                ('user', models.CharField(max_length=30, null=True, blank=True)),
                ('posting_live', models.NullBooleanField(default=False)),
                ('more_info', models.CharField(max_length=3000, null=True, blank=True)),
                ('docfile2', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('docfile3', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('docfile4', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('online_search_live', models.NullBooleanField(default=False)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2015, 4, 3, 1, 23, 44, 654464))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='whichsite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site', models.CharField(max_length=3000, null=True, blank=True)),
                ('item', models.CharField(max_length=3000, null=True, blank=True)),
                ('a_ref', models.CharField(max_length=1000, null=True, blank=True)),
                ('a_ref_name', models.CharField(max_length=3000, null=True, blank=True)),
                ('price', models.DecimalField(max_length=30, null=True, max_digits=10, decimal_places=4, blank=True)),
                ('condition', models.CharField(max_length=30000, null=True, blank=True)),
                ('distance', models.DecimalField(max_length=30, null=True, max_digits=10, decimal_places=4, blank=True)),
                ('price_pres', models.CharField(max_length=30, null=True, blank=True)),
                ('user_item', models.CharField(max_length=30, null=True, blank=True)),
                ('user', models.CharField(max_length=30, null=True, blank=True)),
                ('zipcode', models.DecimalField(max_length=30, null=True, max_digits=10, decimal_places=4, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
