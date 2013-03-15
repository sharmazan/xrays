# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Specialist'
        db.create_table(u'catalog_specialist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('speciality', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('info', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'catalog', ['Specialist'])

        # Adding model 'Patient'
        db.create_table(u'catalog_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('info', self.gf('django.db.models.fields.TextField')()),
            ('history', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Specialist'])),
        ))
        db.send_create_signal(u'catalog', ['Patient'])

        # Adding model 'Survey'
        db.create_table(u'catalog_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Patient'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('result', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('technician', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Specialist'])),
        ))
        db.send_create_signal(u'catalog', ['Survey'])


    def backwards(self, orm):
        # Deleting model 'Specialist'
        db.delete_table(u'catalog_specialist')

        # Deleting model 'Patient'
        db.delete_table(u'catalog_patient')

        # Deleting model 'Survey'
        db.delete_table(u'catalog_survey')


    models = {
        u'catalog.patient': {
            'Meta': {'object_name': 'Patient'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Specialist']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'history': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'catalog.specialist': {
            'Meta': {'object_name': 'Specialist'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'catalog.survey': {
            'Meta': {'object_name': 'Survey'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Patient']"}),
            'result': ('django.db.models.fields.TextField', [], {}),
            'technician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Specialist']"})
        }
    }

    complete_apps = ['catalog']