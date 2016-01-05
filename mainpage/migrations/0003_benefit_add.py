# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_benefit_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit_add',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
        ),
    ]
