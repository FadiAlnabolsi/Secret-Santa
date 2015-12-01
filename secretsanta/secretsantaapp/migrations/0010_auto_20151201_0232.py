# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secretsantaapp', '0009_auto_20151128_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('giver', models.ForeignKey(related_name='giver_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='SecretSantaGroups',
            new_name='SecretSantaGroup',
        ),
        migrations.RemoveField(
            model_name='assignees',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='assignees',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='assignees',
            name='group',
        ),
        migrations.RenameField(
            model_name='secretsantagroup',
            old_name='groupName',
            new_name='group_name',
        ),
        migrations.DeleteModel(
            name='assignees',
        ),
        migrations.AddField(
            model_name='assignment',
            name='group',
            field=models.ForeignKey(to='secretsantaapp.SecretSantaGroup'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='receiver',
            field=models.ForeignKey(related_name='receiver_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
