# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_benefit_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection_step',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('step_number', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
        ),
    ]
