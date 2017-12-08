# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_auto_20150817_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_emails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site', models.CharField(max_length=3000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
