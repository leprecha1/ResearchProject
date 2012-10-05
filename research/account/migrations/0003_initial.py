# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'actors'
        db.create_table('account_actors', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('passwd', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('rank', self.gf('django.db.models.fields.IntegerField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('account', ['actors'])

        # Adding model 'research'
        db.create_table('account_research', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('start_at', self.gf('django.db.models.fields.DateField')()),
            ('finish_at', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('account', ['research'])


    def backwards(self, orm):
        # Deleting model 'actors'
        db.delete_table('account_actors')

        # Deleting model 'research'
        db.delete_table('account_research')


    models = {
        'account.actors': {
            'Meta': {'object_name': 'actors'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'passwd': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'rank': ('django.db.models.fields.IntegerField', [], {})
        },
        'account.research': {
            'Meta': {'object_name': 'research'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'finish_at': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_at': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['account']