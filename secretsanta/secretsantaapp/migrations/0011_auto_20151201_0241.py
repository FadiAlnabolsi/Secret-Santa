# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('secretsantaapp', '0010_auto_20151201_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='giver',
            field=models.ForeignKey(related_name='giver_user', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='receiver',
            field=models.ForeignKey(related_name='receiver_user', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
