# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Seed.metadata'
        db.alter_column('archiveit_seed', 'metadata', self.gf('jsonfield.fields.JSONField')(null=True))

        # Changing field 'Collection.metadata'
        db.alter_column('archiveit_collection', 'metadata', self.gf('jsonfield.fields.JSONField')())

        # Changing field 'Document.metadata'
        db.alter_column('archiveit_document', 'metadata', self.gf('jsonfield.fields.JSONField')(null=True))

        # Changing field 'Crawl.metadata'
        db.alter_column('archiveit_crawl', 'metadata', self.gf('jsonfield.fields.JSONField')(null=True))

    def backwards(self, orm):

        # Changing field 'Seed.metadata'
        db.alter_column('archiveit_seed', 'metadata', self.gf('picklefield.fields.PickledObjectField')(null=True))

        # Changing field 'Collection.metadata'
        db.alter_column('archiveit_collection', 'metadata', self.gf('picklefield.fields.PickledObjectField')())

        # Changing field 'Document.metadata'
        db.alter_column('archiveit_document', 'metadata', self.gf('picklefield.fields.PickledObjectField')(null=True))

        # Changing field 'Crawl.metadata'
        db.alter_column('archiveit_crawl', 'metadata', self.gf('picklefield.fields.PickledObjectField')(null=True))

    models = {
        'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'storage_quota': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['accounts.StorageQuota']", 'unique': 'True'}),
            'up_to_date': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_quota': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'accounts.storagequota': {
            'Meta': {'object_name': 'StorageQuota'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'archiveit.collection': {
            'Meta': {'object_name': 'Collection'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_crawl': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'metadata': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Account']", 'blank': 'True', 'null': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'topics': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.CollectionTopic']", 'blank': 'True', 'null': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
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
            'metadata': ('jsonfield.fields.JSONField', [], {'blank': 'True', 'null': 'True'}),
            'seed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Seed']"})
        },
        'archiveit.document': {
            'Meta': {'object_name': 'Document'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'crawl': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Crawl']"}),
            'fetch_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('jsonfield.fields.JSONField', [], {'blank': 'True', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'archiveit.seed': {
            'Meta': {'object_name': 'Seed'},
            'capture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.SeedCapturePattern']", 'blank': 'True', 'null': 'True'}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Collection']"}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.SeedFolder']", 'blank': 'True', 'null': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.SeedGroup']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('jsonfield.fields.JSONField', [], {'blank': 'True', 'null': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'archiveit.seedcapturepattern': {
            'Meta': {'object_name': 'SeedCapturePattern'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pattern': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'archiveit.seedfolder': {
            'Meta': {'object_name': 'SeedFolder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.SeedFolder']", 'blank': 'True', 'null': 'True', 'related_name': "'children'"})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['archiveit']