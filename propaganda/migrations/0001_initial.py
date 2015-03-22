# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pamphlet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_date', models.DateField(verbose_name='delivery date')),
                ('sent', models.BooleanField(default=False, verbose_name='sent pamphlet')),
            ],
            options={
                'verbose_name': 'pamphlet',
                'verbose_name_plural': 'pamphlets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Propaganda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plaintext_msg', models.TextField(verbose_name='plain text message')),
                ('html_msg', models.TextField(verbose_name='html message')),
                ('subject', models.CharField(max_length=255, verbose_name='subject')),
                ('from_header', models.CharField(max_length=255, verbose_name='sender name', blank=True)),
            ],
            options={
                'verbose_name': 'propaganda',
                'verbose_name_plural': 'propagandas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name='email')),
                ('active', models.BooleanField(default=True, verbose_name='active user')),
                ('test_user', models.BooleanField(default=False, verbose_name='test user')),
            ],
            options={
                'verbose_name': 'subscriber',
                'verbose_name_plural': 'subscribers',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pamphlet',
            name='propaganda',
            field=models.ForeignKey(verbose_name='propaganda', to='propaganda.Propaganda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pamphlet',
            name='subscriber',
            field=models.ForeignKey(verbose_name='subscriber', to='propaganda.Subscriber'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='pamphlet',
            unique_together=set([('subscriber', 'propaganda', 'delivery_date')]),
        ),
    ]
