# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretsantaapp', '0006_auto_20151128_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignees',
            name='assignee',
            field=models.ForeignKey(related_name='members2', to='secretsantaapp.SecretSantaGroups', null=True),
        ),
        migrations.AddField(
            model_name='assignees',
            name='creator',
            field=models.ForeignKey(related_name='members1', to='secretsantaapp.SecretSantaGroups', null=True),
        ),
    ]
