# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_id',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='question',
            name='question_id',
            field=models.CharField(default=True, max_length=30, serialize=False, primary_key=True),
        ),
    ]
