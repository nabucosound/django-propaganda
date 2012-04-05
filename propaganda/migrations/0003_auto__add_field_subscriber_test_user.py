# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Subscriber.test_user'
        db.add_column('propaganda_subscriber', 'test_user',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Subscriber.test_user'
        db.delete_column('propaganda_subscriber', 'test_user')

    models = {
        'propaganda.pamphlet': {
            'Meta': {'unique_together': "(('subscriber', 'propaganda', 'delivery_date'),)", 'object_name': 'Pamphlet'},
            'delivery_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propaganda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propaganda.Propaganda']"}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propaganda.Subscriber']"})
        },
        'propaganda.propaganda': {
            'Meta': {'object_name': 'Propaganda'},
            'from_header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'html_msg': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plaintext_msg': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'propaganda.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['propaganda']