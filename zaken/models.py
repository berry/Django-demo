from django.db import models
from django import forms

from djangodemo.subjecten.models import Subject

# Models
ZAAK_TYPEN = (
	('product_A', 'aanvraag product A'),
	('product_B', 'aanvraag product B'),
	('product_C', 'aanvraag product C'),
	)

class Zaak(models.Model):
	subject = models.ForeignKey(Subject)
	datum_start = models.DateTimeField(auto_now_add = True)
	datum_wijziging = models.DateTimeField(auto_now = True)
	type_zaak = models.CharField(max_length = 10, choices = ZAAK_TYPEN)
	opmerkingen = models.TextField()
	
	class Meta:
		verbose_name_plural = "zaken"
		
	def __unicode__(self):
		return "%s" % (self.type_zaak,)

class TypeStap(models.Model):
	type_zaak = models.CharField(max_length = 10, choices = ZAAK_TYPEN)
	type_stap = models.CharField(max_length = 10)
	omschrijving = models.CharField(max_length = 100)
	
	class Meta:
		verbose_name_plural = "typestappen"

class TypeStatus(models.Model):
	type_zaak = models.CharField(max_length = 10, choices = ZAAK_TYPEN)
	type_status = models.CharField(max_length = 10)
	omschrijving = models.CharField(max_length = 100)
	
	class Meta:
		verbose_name_plural = "typestatussen"

class Stap(models.Model):
	'''Voor het afhandelen van een zaak kunnen 1 of 
	meerdere stappen worden gezet. In welke volgorde 
	welke stap gezet wordt, wordt niet afgedwongen 
	door het model. Maar, wordt overgelaten aan een 
	proces buiten het model.'''
	
	zaak = models.ForeignKey(Zaak)
	type_stap = models.ForeignKey(TypeStap)
	datum_start = models.DateTimeField(auto_now_add = True)
	datum_afgerond = models.DateTimeField(null = True, blank = True)
	opmerkingen = models.TextField(null = True, blank = True)
	
	class Meta:
		verbose_name_plural = "stappen"

class Status(models.Model):
	'''Bij het zetten van stappen voor het afhandelen 
	van een zaak kan een bepaalde status worden bereikt. 
	Bij welke stappen welke status wordt bereikt wordt 
	vastgelegd en gemanaged buiten het model om.'''
	
	zaak = models.ForeignKey(Zaak)
	type_status = models.ForeignKey(TypeStatus)
	datum = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		verbose_name_plural = "statussen"

# Forms
class NewZaakForSubjectForm(forms.Form):
	type_zaak = forms.ChoiceField(label="Type zaak", choices = ZAAK_TYPEN)
	opmerkingen = forms.CharField(label="Opmerkingen", widget=forms.Textarea)

