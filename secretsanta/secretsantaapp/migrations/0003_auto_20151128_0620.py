# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secretsantaapp', '0002_auto_20151128_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretSantaGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.TextField()),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Secret Santa Groups',
            },
        ),
        migrations.RemoveField(
            model_name='groups',
            name='user',
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
    ]
