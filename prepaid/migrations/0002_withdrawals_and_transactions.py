
from south.db import db
from django.db import models
from prepaid.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Transaction'
        db.create_table('prepaid_transaction', (
            ('id', orm['prepaid.transaction:id']),
            ('user', orm['prepaid.transaction:user']),
            ('date', orm['prepaid.transaction:date']),
            ('amount', orm['prepaid.transaction:amount']),
            ('total', orm['prepaid.transaction:total']),
            ('credit', orm['prepaid.transaction:credit']),
            ('info', orm['prepaid.transaction:info']),
        ))
        db.send_create_signal('prepaid', ['Transaction'])
        
        # Adding model 'Withdrawal'
        db.create_table('prepaid_withdrawal', (
            ('id', orm['prepaid.withdrawal:id']),
            ('date', orm['prepaid.withdrawal:date']),
            ('user', orm['prepaid.withdrawal:user']),
            ('email', orm['prepaid.withdrawal:email']),
            ('points', orm['prepaid.withdrawal:points']),
            ('approved', orm['prepaid.withdrawal:approved']),
        ))
        db.send_create_signal('prepaid', ['Withdrawal'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Transaction'
        db.delete_table('prepaid_transaction')
        
        # Deleting model 'Withdrawal'
        db.delete_table('prepaid_withdrawal')
        
    
    
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
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'prepaid.transaction': {
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'credit': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prepaid_transactions'", 'to': "orm['auth.User']"})
        },
        'prepaid.unitpack': {
            'expires': ('django.db.models.fields.DateField', [], {'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'prepaid.withdrawal': {
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'withdrawals'", 'to': "orm['auth.User']"})
        }
    }
    
    complete_apps = ['prepaid']
