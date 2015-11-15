# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20151115_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=1, null=True, choices=[(b'F', b'Female'), (b'M', b'Male')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(max_length=2, null=True, choices=[(b'UN', b'UnderGraduate'), (b'GR', b'Graduate')]),
        ),
    ]
