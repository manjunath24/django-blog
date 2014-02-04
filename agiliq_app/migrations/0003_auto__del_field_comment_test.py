# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Comment.test'
        db.delete_column(u'agiliq_app_comment', 'test')


    def backwards(self, orm):
        # Adding field 'Comment.test'
        db.add_column(u'agiliq_app_comment', 'test',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=1),
                      keep_default=False)


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