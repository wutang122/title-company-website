# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_auto_20150817_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='email_subscribers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('message', models.CharField(max_length=300, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='personal_info',
        ),
        migrations.DeleteModel(
            name='user_emails',
        ),
    ]
