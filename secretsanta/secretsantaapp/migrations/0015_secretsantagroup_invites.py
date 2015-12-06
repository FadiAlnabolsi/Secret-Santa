# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secretsantaapp', '0014_secretsantagroup_assignments_generated'),
    ]

    operations = [
        migrations.AddField(
            model_name='secretsantagroup',
            name='invites',
            field=models.ManyToManyField(related_name='invites_sent', to=settings.AUTH_USER_MODEL),
        ),
    ]
