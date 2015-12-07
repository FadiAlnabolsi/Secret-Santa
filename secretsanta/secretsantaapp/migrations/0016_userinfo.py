# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secretsantaapp', '0015_secretsantagroup_invites'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('groups', models.ManyToManyField(to='secretsantaapp.SecretSantaGroup', related_name='participating_in')),
                ('invites', models.ManyToManyField(to='secretsantaapp.SecretSantaGroup', related_name='invited_to')),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
