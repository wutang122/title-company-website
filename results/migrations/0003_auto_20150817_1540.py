# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_auto_20150403_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='personal_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=50, null=True, blank=True)),
                ('lastname', models.DecimalField(max_length=30, null=True, max_digits=8, decimal_places=3, blank=True)),
                ('address', models.CharField(max_length=300, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=300, null=True, blank=True)),
                ('City', models.CharField(max_length=300, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='posting_system',
        ),
        migrations.DeleteModel(
            name='postinglisting',
        ),
        migrations.DeleteModel(
            name='whichsite',
        ),
    ]
