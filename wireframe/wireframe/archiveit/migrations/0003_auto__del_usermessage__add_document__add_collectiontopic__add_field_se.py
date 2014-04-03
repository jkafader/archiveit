# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserMessage'
        db.delete_table('archiveit_usermessage')

        # Adding model 'Document'
        db.create_table('archiveit_document', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crawl', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.Crawl'])),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('fetch_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('metadata', self.gf('picklefield.fields.PickledObjectField')(null=True, blank=True)),
        ))
        db.send_create_signal('archiveit', ['Document'])

        # Adding model 'CollectionTopic'
        db.create_table('archiveit_collectiontopic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('archiveit', ['CollectionTopic'])

        # Adding field 'Seed.metadata'
        db.add_column('archiveit_seed', 'metadata',
                      self.gf('picklefield.fields.PickledObjectField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Seed.group'
        db.alter_column('archiveit_seed', 'group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.SeedGroup'], null=True))

        # Changing field 'Seed.folder'
        db.alter_column('archiveit_seed', 'folder_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.SeedFolder'], null=True))
        # Adding field 'Crawl.metadata'
        db.add_column('archiveit_crawl', 'metadata',
                      self.gf('picklefield.fields.PickledObjectField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.owner'
        db.add_column('archiveit_collection', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.active'
        db.add_column('archiveit_collection', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Collection.topics'
        db.add_column('archiveit_collection', 'topics',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.CollectionTopic'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.created_on'
        db.add_column('archiveit_collection', 'created_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Collection.updated_on'
        db.add_column('archiveit_collection', 'updated_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SeedFolder.owner'
        db.add_column('archiveit_seedfolder', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'SeedFolder.parent'
        db.alter_column('archiveit_seedfolder', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.SeedFolder'], null=True))

    def backwards(self, orm):
        # Adding model 'UserMessage'
        db.create_table('archiveit_usermessage', (
            ('message', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('archiveit', ['UserMessage'])

        # Deleting model 'Document'
        db.delete_table('archiveit_document')

        # Deleting model 'CollectionTopic'
        db.delete_table('archiveit_collectiontopic')

        # Deleting field 'Seed.metadata'
        db.delete_column('archiveit_seed', 'metadata')


        # User chose to not deal with backwards NULL issues for 'Seed.group'
        raise RuntimeError("Cannot reverse this migration. 'Seed.group' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Seed.group'
        db.alter_column('archiveit_seed', 'group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archiveit.SeedGroup']))

        # Changing field 'Seed.folder'
        db.alter_column('archiveit_seed', 'folder_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['archiveit.SeedFolder']))
        # Deleting field 'Crawl.metadata'
        db.delete_column('archiveit_crawl', 'metadata')

        # Deleting field 'Collection.owner'
        db.delete_column('archiveit_collection', 'owner_id')

        # Deleting field 'Collection.active'
        db.delete_column('archiveit_collection', 'active')

        # Deleting field 'Collection.topics'
        db.delete_column('archiveit_collection', 'topics_id')

        # Deleting field 'Collection.created_on'
        db.delete_column('archiveit_collection', 'created_on')

        # Deleting field 'Collection.updated_on'
        db.delete_column('archiveit_collection', 'updated_on')

        # Deleting field 'SeedFolder.owner'
        db.delete_column('archiveit_seedfolder', 'owner_id')


        # Changing field 'SeedFolder.parent'
        db.alter_column('archiveit_seedfolder', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['archiveit.SeedFolder']))

    models = {
        'archiveit.collection': {
            'Meta': {'object_name': 'Collection'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('picklefield.fields.PickledObjectField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'topics': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.CollectionTopic']", 'null': 'True', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'archiveit.collectiontopic': {
            'Meta': {'object_name': 'CollectionTopic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'metadata': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'seed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Seed']"})
        },
        'archiveit.document': {
            'Meta': {'object_name': 'Document'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'crawl': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Crawl']"}),
            'fetch_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'archiveit.seed': {
            'Meta': {'object_name': 'Seed'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Collection']"}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.SeedFolder']", 'null': 'True', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.SeedGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'archiveit.seedfolder': {
            'Meta': {'object_name': 'SeedFolder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.SeedFolder']", 'null': 'True', 'related_name': "'children'", 'blank': 'True'})
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
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['archiveit']