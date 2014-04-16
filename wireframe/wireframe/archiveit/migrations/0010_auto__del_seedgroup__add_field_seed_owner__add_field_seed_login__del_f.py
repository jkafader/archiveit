# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SeedGroup'
        db.delete_table('archiveit_seedgroup')

        # Adding field 'Seed.owner'
        db.add_column('archiveit_seed', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['accounts.Account']),
                      keep_default=False)

        # Adding field 'Seed.login'
        db.add_column('archiveit_seed', 'login',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Removing M2M table for field groups on 'Seed'
        db.delete_table(db.shorten_name('archiveit_seed_groups'))

        # Deleting field 'SeedFolder.parent'
        db.delete_column('archiveit_seedfolder', 'parent_id')


        # Changing field 'SeedFolder.owner'
        db.alter_column('archiveit_seedfolder', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.Account']))

    def backwards(self, orm):
        # Adding model 'SeedGroup'
        db.create_table('archiveit_seedgroup', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('archiveit', ['SeedGroup'])

        # Deleting field 'Seed.owner'
        db.delete_column('archiveit_seed', 'owner_id')

        # Deleting field 'Seed.login'
        db.delete_column('archiveit_seed', 'login')

        # Adding M2M table for field groups on 'Seed'
        m2m_table_name = db.shorten_name('archiveit_seed_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('seed', models.ForeignKey(orm['archiveit.seed'], null=False)),
            ('seedgroup', models.ForeignKey(orm['archiveit.seedgroup'], null=False))
        ))
        db.create_unique(m2m_table_name, ['seed_id', 'seedgroup_id'])

        # Adding field 'SeedFolder.parent'
        db.add_column('archiveit_seedfolder', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='children', to=orm['archiveit.SeedFolder'], blank=True),
                      keep_default=False)


        # Changing field 'SeedFolder.owner'
        db.alter_column('archiveit_seedfolder', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

    models = {
        'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''", 'blank': 'True'}),
            'storage_quota': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['accounts.StorageQuota']"}),
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
            'created_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_crawl': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'metadata': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['accounts.Account']"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'topics': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['archiveit.CollectionTopic']"}),
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
            'metadata': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'seed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Seed']"})
        },
        'archiveit.document': {
            'Meta': {'object_name': 'Document'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'crawl': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Crawl']"}),
            'fetch_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'archiveit.seed': {
            'Meta': {'object_name': 'Seed'},
            'capture': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['archiveit.SeedCapturePattern']"}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archiveit.Collection']"}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['archiveit.SeedFolder']"}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'metadata': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['accounts.Account']"}),
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
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['accounts.Account']"})
        },
        'archiveit.seedscoperule': {
            'Meta': {'object_name': 'SeedScopeRule'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['archiveit.Collection']"}),
            'document_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'default': '10000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rule_match': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'rule_type': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'seeds': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'symmetrical': 'False', 'blank': 'True', 'to': "orm['archiveit.Seed']"}),
            'use_document_limit': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['archiveit']