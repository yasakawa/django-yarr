# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

# Custom user support
try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
else:
    User = get_user_model()
user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)
user_model_label = '%s.%s' % (User._meta.app_label, User._meta.module_name)


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feed'
        db.create_table('yarr_feed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('feed_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('site_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[user_orm_label])),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('check_frequency', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_checked', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('next_check', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('error', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('yarr', ['Feed'])

        # Adding model 'Entry'
        db.create_table('yarr_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['yarr.Feed'])),
            ('read', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('saved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('comments_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('guid', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('yarr', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'Feed'
        db.delete_table('yarr_feed')

        # Deleting model 'Entry'
        db.delete_table('yarr_entry')


    models = {
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
        user_model_label: {
            'Meta': {
                'object_name': User.__name__,
                'db_table': "'%s'" % User._meta.db_table
            },
            User._meta.pk.attname: (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True',
                'db_column': "'%s'" % User._meta.pk.column}
            ),
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'yarr.entry': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Entry'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'comments_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['yarr.Feed']"}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'saved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'yarr.feed': {
            'Meta': {'ordering': "('title', 'added')", 'object_name': 'Feed'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'check_frequency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'error': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'feed_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_checked': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'next_check': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['%s']" % user_orm_label})
        }
    }

    complete_apps = ['yarr']