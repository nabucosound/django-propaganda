# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pamphlet.sent'
        db.add_column('propaganda_pamphlet', 'sent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Pamphlet.delivery_date'
        db.alter_column('propaganda_pamphlet', 'delivery_date', self.gf('django.db.models.fields.DateField')())
    def backwards(self, orm):
        # Deleting field 'Pamphlet.sent'
        db.delete_column('propaganda_pamphlet', 'sent')


        # Changing field 'Pamphlet.delivery_date'
        db.alter_column('propaganda_pamphlet', 'delivery_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
    models = {
        'propaganda.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'propaganda.pamphlet': {
            'Meta': {'unique_together': "(('subscriber', 'propaganda', 'delivery_date'),)", 'object_name': 'Pamphlet'},
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propaganda.Subscriber']"}),
            'delivery_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propaganda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propaganda.Propaganda']"}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'propaganda.propaganda': {
            'Meta': {'object_name': 'Propaganda'},
            'from_header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'html_msg': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plaintext_msg': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['propaganda']
