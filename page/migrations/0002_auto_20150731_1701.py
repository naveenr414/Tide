# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(default='000000', to='page.Category'),
            preserve_default=False,
        ),
    ]
