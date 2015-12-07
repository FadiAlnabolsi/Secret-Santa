# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretsantaapp', '0016_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='participating_in', to='secretsantaapp.SecretSantaGroup'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='invites',
            field=models.ManyToManyField(blank=True, related_name='invited_to', to='secretsantaapp.SecretSantaGroup'),
        ),
    ]
