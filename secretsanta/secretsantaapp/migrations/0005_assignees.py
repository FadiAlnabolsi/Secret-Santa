# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretsantaapp', '0004_auto_20151128_0621'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignees',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('group', models.ForeignKey(to='secretsantaapp.SecretSantaGroups')),
            ],
        ),
    ]
