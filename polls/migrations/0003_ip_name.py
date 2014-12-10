# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20140522_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='name',
            field=models.CharField(max_length=100, default=datetime.date(2014, 5, 23)),
            preserve_default=False,
        ),
    ]
