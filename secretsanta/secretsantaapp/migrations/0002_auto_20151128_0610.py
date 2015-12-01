# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secretsantaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name_plural': 'Secret Santa Groups'},
        ),
        migrations.RemoveField(
            model_name='groups',
            name='users',
        ),
        migrations.AddField(
            model_name='groups',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, to_field='username', related_name='commented_on'),
            preserve_default=False,
        ),
    ]
