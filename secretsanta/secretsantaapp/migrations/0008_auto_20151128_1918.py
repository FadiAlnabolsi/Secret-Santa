# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretsantaapp', '0007_auto_20151128_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignees',
            name='assignee',
            field=models.ForeignKey(related_name='mem2', null=True, to='secretsantaapp.SecretSantaGroups'),
        ),
        migrations.AlterField(
            model_name='assignees',
            name='creator',
            field=models.ForeignKey(related_name='mem1', null=True, to='secretsantaapp.SecretSantaGroups'),
        ),
    ]
