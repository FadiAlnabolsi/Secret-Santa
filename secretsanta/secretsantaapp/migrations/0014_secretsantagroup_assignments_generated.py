# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretsantaapp', '0013_secretsantagroup_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='secretsantagroup',
            name='assignments_generated',
            field=models.BooleanField(default=False),
        ),
    ]
