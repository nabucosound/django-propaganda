# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Propaganda'
        db.create_table('propaganda_propaganda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plaintext_msg', self.gf('django.db.models.fields.TextField')()),
            ('html_msg', self.gf('django.db.models.fields.TextField')()),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('from_header', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('propaganda', ['Propaganda'])

        # Adding model 'Subscriber'
        db.create_table('propaganda_subscriber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('propaganda', ['Subscriber'])

        # Adding model 'Pamphlet'
        db.create_table('propaganda_pamphlet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subscriber', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['propaganda.Subscriber'])),
            ('propaganda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['propaganda.Propaganda'])),
            ('delivery_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('propaganda', ['Pamphlet'])

        # Adding unique constraint on 'Pamphlet', fields ['subscriber', 'propaganda', 'delivery_date']
        db.create_unique('propaganda_pamphlet', ['subscriber_id', 'propaganda_id', 'delivery_date'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Pamphlet', fields ['subscriber', 'propaganda', 'delivery_date']
        db.delete_unique('propaganda_pamphlet', ['subscriber_id', 'propaganda_id', 'delivery_date'])

        # Deleting model 'Propaganda'
        db.delete_table('propaganda_propaganda')

        # Deleting model 'Subscriber'
        db.delete_table('propaganda_subscriber')

        # Deleting model 'Pamphlet'
        db.delete_table('propaganda_pamphlet')


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
            'delivery_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propaganda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propaganda.Propaganda']"})
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
