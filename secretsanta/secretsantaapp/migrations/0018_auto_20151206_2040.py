# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('secretsantaapp', '0017_auto_20151206_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretsantagroup',
            name='invites',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='invites_sent'),
        ),
        migrations.AlterField(
            model_name='secretsantagroup',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
