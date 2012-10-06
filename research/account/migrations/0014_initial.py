# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'research'
        db.create_table('account_research', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('start_at', self.gf('django.db.models.fields.DateField')()),
            ('finish_at', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('publish', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('account', ['research'])

        # Adding model 'multiple_choice'
        db.create_table('account_multiple_choice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alt_1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('alt_2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('alt_3', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('account', ['multiple_choice'])


    def backwards(self, orm):
        # Deleting model 'research'
        db.delete_table('account_research')

        # Deleting model 'multiple_choice'
        db.delete_table('account_multiple_choice')


    models = {
        'account.multiple_choice': {
            'Meta': {'object_name': 'multiple_choice'},
            'alt_1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'alt_2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'alt_3': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'account.research': {
            'Meta': {'object_name': 'research'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'finish_at': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'start_at': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['account']