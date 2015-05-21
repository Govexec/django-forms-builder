# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20150519_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='sites',
            field=models.ManyToManyField(default=[4], related_name='forms_form_forms', editable=False, to='sites.Site'),
        ),
    ]
