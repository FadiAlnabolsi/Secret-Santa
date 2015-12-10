# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretsantaapp', '0019_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='list',
            new_name='user',
        ),
    ]
