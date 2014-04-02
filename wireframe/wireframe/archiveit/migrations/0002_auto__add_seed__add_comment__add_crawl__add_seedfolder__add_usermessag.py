# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Seed'
        db.create_table('archiveit_seed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.Collection'])),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('public', self.gf('django.db.models.fields.BooleanField')()),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.SeedGroup'])),
            ('folder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.SeedFolder'])),
        ))
        db.send_create_signal('archiveit', ['Seed'])

        # Adding model 'Comment'
        db.create_table('archiveit_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('archiveit', ['Comment'])

        # Adding model 'Crawl'
        db.create_table('archiveit_crawl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.Seed'])),
            ('begun_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('ended_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('completed', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('archiveit', ['Crawl'])

        # Adding model 'SeedFolder'
        db.create_table('archiveit_seedfolder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.SeedFolder'], related_name='children')),
        ))
        db.send_create_signal('archiveit', ['SeedFolder'])

        # Adding model 'UserMessage'
        db.create_table('archiveit_usermessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('archiveit', ['UserMessage'])

        # Adding model 'SeedScopeRule'
        db.create_table('archiveit_seedscoperule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rule_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('rule_match', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('document_limit', self.gf('django.db.models.fields.BooleanField')()),
            ('use_document_limit', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('archiveit', ['SeedScopeRule'])

        # Adding model 'SeedGroup'
        db.create_table('archiveit_seedgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('archiveit', ['SeedGroup'])

        # Adding model 'Collection'
        db.create_table('archiveit_collection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('public', self.gf('django.db.models.fields.BooleanField')()),
            ('metadata', self.gf('picklefield.fields.PickledObjectField')()),
        ))
        db.send_create_signal('archiveit', ['Collection'])


    def backwards(self, orm):
        # Deleting model 'Seed'
        db.delete_table('archiveit_seed')

        # Deleting model 'Comment'
        db.delete_table('archiveit_comment')

        # Deleting model 'Crawl'
        db.delete_table('archiveit_crawl')

        # Deleting model 'SeedFolder'
        db.delete_table('archiveit_seedfolder')

        # Deleting model 'UserMessage'
        db.delete_table('archiveit_usermessage')

        # Deleting model 'SeedScopeRule'
        db.delete_table('archiveit_seedscoperule')

        # Deleting model 'SeedGroup'
        db.delete_table('archiveit_seedgroup')

        # Deleting model 'Collection'
        db.delete_table('archiveit_collection')


    models = {
        'archiveit.collection': {
            'Meta': {'object_name': 'Collection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('picklefield.fields.PickledObjectField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'public': ('django.db.models.fields.BooleanField', [], {})
        },
        'archiveit.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'archiveit.crawl': {
            'Meta': {'object_name': 'Crawl'},
            'begun_on': ('django.db.models.fields.DateTimeField', [], {}),
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'ended_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Seed']"})
        },
        'archiveit.seed': {
            'Meta': {'object_name': 'Seed'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Collection']"}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.SeedFolder']"}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.SeedGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'archiveit.seedfolder': {
            'Meta': {'object_name': 'SeedFolder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.SeedFolder']", 'related_name': "'children'"})
        },
        'archiveit.seedgroup': {
            'Meta': {'object_name': 'SeedGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'archiveit.seedscoperule': {
            'Meta': {'object_name': 'SeedScopeRule'},
            'document_limit': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rule_match': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rule_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'use_document_limit': ('django.db.models.fields.IntegerField', [], {})
        },
        'archiveit.usermessage': {
            'Meta': {'object_name': 'UserMessage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['archiveit']