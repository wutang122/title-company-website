# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting_system',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 3, 1, 33, 25, 417202)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postinglisting',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 3, 1, 33, 25, 416297)),
            preserve_default=True,
        ),
    ]
