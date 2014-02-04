# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'agiliq_app_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('blog_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'agiliq_app', ['Article'])

        # Adding model 'Comment'
        db.create_table(u'agiliq_app_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blogid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agiliq_app.Article'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dessription', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default=0, max_length=1)),
        ))
        db.send_create_signal(u'agiliq_app', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'agiliq_app_article')

        # Deleting model 'Comment'
        db.delete_table(u'agiliq_app_comment')


    models = {
        u'agiliq_app.article': {
            'Meta': {'object_name': 'Article'},
            'blog_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'agiliq_app.comment': {
            'Meta': {'object_name': 'Comment'},
            'blogid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agiliq_app.Article']"}),
            'dessription': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '1'})
        }
    }

    complete_apps = ['agiliq_app']