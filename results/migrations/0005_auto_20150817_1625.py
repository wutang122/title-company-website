# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_user_emails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_emails',
            old_name='site',
            new_name='email',
        ),
    ]
