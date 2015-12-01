# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretsantaapp', '0008_auto_20151128_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignees',
            name='assignee',
            field=models.OneToOneField(to='secretsantaapp.SecretSantaGroups', null=True, related_name='mem2'),
        ),
        migrations.AlterField(
            model_name='assignees',
            name='creator',
            field=models.OneToOneField(to='secretsantaapp.SecretSantaGroups', null=True, related_name='mem1'),
        ),
    ]
