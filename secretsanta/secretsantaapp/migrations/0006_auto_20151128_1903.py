# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretsantaapp', '0005_assignees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secretsantagroups',
            old_name='users',
            new_name='members',
        ),
    ]
