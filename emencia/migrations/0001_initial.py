from south.db import db
from django.db import models
from emencia.models import *

class Migration:

    def forwards(self, orm):

        # Adding model 'MailingList'
        db.create_table('emencia_mailinglist', (
            ('id', orm['emencia.MailingList:id']),
            ('name', orm['emencia.MailingList:name']),
            ('description', orm['emencia.MailingList:description']),
            ('creation_date', orm['emencia.MailingList:creation_date']),
            ('modification_date', orm['emencia.MailingList:modification_date']),
        ))
        db.send_create_signal('emencia', ['MailingList'])

        # Adding model 'ContactMailingStatus'
        db.create_table('emencia_contactmailingstatus', (
            ('id', orm['emencia.ContactMailingStatus:id']),
            ('newsletter', orm['emencia.ContactMailingStatus:newsletter']),
            ('contact', orm['emencia.ContactMailingStatus:contact']),
            ('status', orm['emencia.ContactMailingStatus:status']),
            ('link', orm['emencia.ContactMailingStatus:link']),
            ('creation_date', orm['emencia.ContactMailingStatus:creation_date']),
        ))
        db.send_create_signal('emencia', ['ContactMailingStatus'])

        # Adding model 'WorkGroup'
        db.create_table('emencia_workgroup', (
            ('id', orm['emencia.WorkGroup:id']),
            ('name', orm['emencia.WorkGroup:name']),
            ('group', orm['emencia.WorkGroup:group']),
        ))
        db.send_create_signal('emencia', ['WorkGroup'])

        # Adding model 'Link'
        db.create_table('emencia_link', (
            ('id', orm['emencia.Link:id']),
            ('title', orm['emencia.Link:title']),
            ('url', orm['emencia.Link:url']),
            ('creation_date', orm['emencia.Link:creation_date']),
        ))
        db.send_create_signal('emencia', ['Link'])

        # Adding model 'Newsletter'
        db.create_table('emencia_newsletter', (
            ('id', orm['emencia.Newsletter:id']),
            ('title', orm['emencia.Newsletter:title']),
            ('content', orm['emencia.Newsletter:content']),
            ('mailing_list', orm['emencia.Newsletter:mailing_list']),
            ('server', orm['emencia.Newsletter:server']),
            ('header_sender', orm['emencia.Newsletter:header_sender']),
            ('header_reply', orm['emencia.Newsletter:header_reply']),
            ('status', orm['emencia.Newsletter:status']),
            ('sending_date', orm['emencia.Newsletter:sending_date']),
            ('slug', orm['emencia.Newsletter:slug']),
            ('creation_date', orm['emencia.Newsletter:creation_date']),
            ('modification_date', orm['emencia.Newsletter:modification_date']),
        ))
        db.send_create_signal('emencia', ['Newsletter'])

        # Adding model 'SMTPServer'
        db.create_table('emencia_smtpserver', (
            ('id', orm['emencia.SMTPServer:id']),
            ('name', orm['emencia.SMTPServer:name']),
            ('host', orm['emencia.SMTPServer:host']),
            ('user', orm['emencia.SMTPServer:user']),
            ('password', orm['emencia.SMTPServer:password']),
            ('port', orm['emencia.SMTPServer:port']),
            ('tls', orm['emencia.SMTPServer:tls']),
            ('headers', orm['emencia.SMTPServer:headers']),
            ('mails_hour', orm['emencia.SMTPServer:mails_hour']),
        ))
        db.send_create_signal('emencia', ['SMTPServer'])

        # Adding model 'Contact'
        db.create_table('emencia_contact', (
            ('id', orm['emencia.Contact:id']),
            ('email', orm['emencia.Contact:email']),
            ('first_name', orm['emencia.Contact:first_name']),
            ('last_name', orm['emencia.Contact:last_name']),
            ('subscriber', orm['emencia.Contact:subscriber']),
            ('valid', orm['emencia.Contact:valid']),
            ('tester', orm['emencia.Contact:tester']),
            ('tags', orm['emencia.Contact:tags']),
            ('content_type', orm['emencia.Contact:content_type']),
            ('object_id', orm['emencia.Contact:object_id']),
            ('creation_date', orm['emencia.Contact:creation_date']),
            ('modification_date', orm['emencia.Contact:modification_date']),
        ))
        db.send_create_signal('emencia', ['Contact'])

        # Adding ManyToManyField 'WorkGroup.mailinglists'
        db.create_table('emencia_workgroup_mailinglists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workgroup', models.ForeignKey(orm.WorkGroup, null=False)),
            ('mailinglist', models.ForeignKey(orm.MailingList, null=False))
        ))

        # Adding ManyToManyField 'MailingList.subscribers'
        db.create_table('emencia_mailinglist_subscribers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mailinglist', models.ForeignKey(orm.MailingList, null=False)),
            ('contact', models.ForeignKey(orm.Contact, null=False))
        ))

        # Adding ManyToManyField 'WorkGroup.contacts'
        db.create_table('emencia_workgroup_contacts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workgroup', models.ForeignKey(orm.WorkGroup, null=False)),
            ('contact', models.ForeignKey(orm.Contact, null=False))
        ))

        # Adding ManyToManyField 'WorkGroup.newsletters'
        db.create_table('emencia_workgroup_newsletters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workgroup', models.ForeignKey(orm.WorkGroup, null=False)),
            ('newsletter', models.ForeignKey(orm.Newsletter, null=False))
        ))

        # Adding ManyToManyField 'MailingList.unsubscribers'
        db.create_table('emencia_mailinglist_unsubscribers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mailinglist', models.ForeignKey(orm.MailingList, null=False)),
            ('contact', models.ForeignKey(orm.Contact, null=False))
        ))

        # Adding ManyToManyField 'emencia.test_contacts'
        db.create_table('emencia_newsletter_test_contacts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsletter', models.ForeignKey(orm.Newsletter, null=False)),
            ('contact', models.ForeignKey(orm.Contact, null=False))
        ))

    def backwards(self, orm):

        # Deleting model 'MailingList'
        db.delete_table('emencia_mailinglist')

        # Deleting model 'ContactMailingStatus'
        db.delete_table('emencia_contactmailingstatus')

        # Deleting model 'WorkGroup'
        db.delete_table('emencia_workgroup')

        # Deleting model 'Link'
        db.delete_table('emencia_link')

        # Deleting model 'Newsletter'
        db.delete_table('emencia_newsletter')

        # Deleting model 'SMTPServer'
        db.delete_table('emencia_smtpserver')

        # Deleting model 'Contact'
        db.delete_table('emencia_contact')

        # Dropping ManyToManyField 'WorkGroup.mailinglists'
        db.delete_table('emencia_workgroup_mailinglists')

        # Dropping ManyToManyField 'MailingList.subscribers'
        db.delete_table('emencia_mailinglist_subscribers')

        # Dropping ManyToManyField 'WorkGroup.contacts'
        db.delete_table('emencia_workgroup_contacts')

        # Dropping ManyToManyField 'WorkGroup.newsletters'
        db.delete_table('emencia_workgroup_newsletters')

        # Dropping ManyToManyField 'MailingList.unsubscribers'
        db.delete_table('emencia_mailinglist_unsubscribers')

        # Dropping ManyToManyField 'emencia.test_contacts'
        db.delete_table('emencia_newsletter_test_contacts')

    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'emencia.contact': {
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'subscriber': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'default': "''"}),
            'tester': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        },
        'emencia.contactmailingstatus': {
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emencia.Contact']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emencia.Link']", 'null': 'True', 'blank': 'True'}),
            'newsletter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emencia.Newsletter']"}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        'emencia.link': {
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'emencia.mailinglist': {
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emencia.Contact']"}),
            'unsubscribers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emencia.Contact']", 'null': 'True', 'blank': 'True'})
        },
        'emencia.newsletter': {
            'content': ('django.db.models.fields.TextField', [], {'default': "u'<body>\\n<!-- Edit your newsletter here -->\\n</body>'"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'header_reply': ('django.db.models.fields.CharField', [], {'default': "'Emencia Newsletter<noreply@emencia.com>'", 'max_length': '255'}),
            'header_sender': ('django.db.models.fields.CharField', [], {'default': "'Emencia Newsletter<noreply@emencia.com>'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emencia.MailingList']"}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sending_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['emencia.SMTPServer']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'test_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emencia.Contact']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'emencia.smtpserver': {
            'headers': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mails_hour': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '25'}),
            'tls': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        'emencia.workgroup': {
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emencia.Contact']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailinglists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emencia.MailingList']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'newsletters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emencia.Newsletter']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['emencia']
