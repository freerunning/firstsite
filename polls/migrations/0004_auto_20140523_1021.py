# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_ip_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='ip',
            field=models.ManyToManyField(blank=True, to='polls.Ip'),
        ),
    ]
