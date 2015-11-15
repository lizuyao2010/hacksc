# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20151115_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
