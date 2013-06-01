# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MailingListSegment'
        db.create_table('emencia_mailinglistsegment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mailing_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emencia.MailingList'])),
        ))
        db.send_create_signal('emencia', ['MailingListSegment'])

        # Adding M2M table for field subscribers on 'MailingListSegment'
        db.create_table('emencia_mailinglistsegment_subscribers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mailinglistsegment', models.ForeignKey(orm['emencia.mailinglistsegment'], null=False)),
            ('contact', models.ForeignKey(orm['emencia.contact'], null=False))
        ))
        db.create_unique('emencia_mailinglistsegment_subscribers', ['mailinglistsegment_id', 'contact_id'])


    def backwards(self, orm):
        # Deleting model 'MailingListSegment'
        db.delete_table('emencia_mailinglistsegment')

        # Removing M2M table for field subscribers on 'MailingListSegment'
        db.delete_table('emencia_mailinglistsegment_subscribers')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'emencia.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'file_attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'newsletter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emencia.Newsletter']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'emencia.contact': {
            'Meta': {'ordering': "('creation_date',)", 'object_name': 'Contact'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'subscriber': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tester': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'emencia.contactmailingstatus': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'ContactMailingStatus'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emencia.Contact']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emencia.Link']", 'null': 'True', 'blank': 'True'}),
            'newsletter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emencia.Newsletter']"}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        'emencia.link': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'Link'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'emencia.mailinglist': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'MailingList'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mailinglist_subscriber'", 'symmetrical': 'False', 'to': "orm['emencia.Contact']"}),
            'unsubscribers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'mailinglist_unsubscriber'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['emencia.Contact']"})
        },
        'emencia.mailinglistsegment': {
            'Meta': {'object_name': 'MailingListSegment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emencia.MailingList']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emencia.Contact']", 'symmetrical': 'False'})
        },
        'emencia.newsletter': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'Newsletter'},
            'content': ('django.db.models.fields.TextField', [], {'default': "u'<body>\\n<!-- Edit your newsletter here -->\\n</body>'"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'header_reply': ('django.db.models.fields.CharField', [], {'default': "'My NewsLetter <newsletter@a2v.eu>'", 'max_length': '255'}),
            'header_sender': ('django.db.models.fields.CharField', [], {'default': "'My NewsLetter <newsletter@a2v.eu>'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emencia.MailingList']", 'null': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sending_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['emencia.SMTPServer']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'test_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['emencia.Contact']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'emencia.smtpserver': {
            'Meta': {'object_name': 'SMTPServer'},
            'emails_remains': ('django.db.models.fields.IntegerField', [], {'default': '10000'}),
            'headers': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mails_hour': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '25'}),
            'tls': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        'emencia.workgroup': {
            'Meta': {'object_name': 'WorkGroup'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['emencia.Contact']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailinglists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['emencia.MailingList']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'newsletters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['emencia.Newsletter']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['emencia']
