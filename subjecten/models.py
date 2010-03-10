import re

from django.db import models
from django import forms

# Models
class Subject(models.Model):
	bsn = models.IntegerField('burger service nummer')
	achternaam = models.CharField(max_length=200)
	voorletters = models.CharField(max_length=15)
	tussenvoegsels = models.CharField(max_length=15)
	woonadres_straatnaam = models.CharField(max_length=200)
	woonadres_huisnummer = models.CharField(max_length=10)
	woonadres_huisnummer_toevoeging = models.CharField(max_length=10)
	woonadres_postcode = models.CharField(max_length=6)
	woonadres_woonplaats = models.CharField(max_length=200)
	correspondentie_straatnaam = models.CharField(max_length=200)
	correspondentie_huisnummer = models.CharField(max_length=10)
	correspondentie_huisnummer_toevoeging = models.CharField(max_length=10)
	correspondentie_postcode = models.CharField(max_length=6)
	correspondentie_woonplaats = models.CharField(max_length=200)
	telefoonnummer = models.CharField(max_length=15)
	email = models.EmailField()
	geboortedatum = models.DateField()
	
	class Meta:
		verbose_name_plural = "subjecten"
		
	def __unicode__(self):
		return "%s %s %s" % (self.voorletters, self.tussenvoegsels, self.achternaam)

# Form validators
class DutchPostcodeField(forms.Field):
	def clean(self, value):
		'''Check that input is a valid Dutch postcode'''
		m = re.match(r'^([0-9]{4})\s?([a-zA-Z]{2}$)', value) # pattern: 1234 AA
		if not m or len(m.groups()) != 2:
			raise forms.ValidationError('Een Nederlandse postcode ziet er als volgt uit: 1234 AA')
		return "%s %s" % (m.groups()[0], m.groups()[1].upper())

class AmsterdamPostcodeField(DutchPostcodeField):
	def clean(self, value):
		'''Check that input is a valid Dutch postcode and 
		check that Dutch postcode is within the Amsterdam 
		postcode ranges.
		'''
		value = super(AmsterdamPostcodeField, self).clean(value)
		n = int(value[0:4])
		if not(1000 <= n <= 1099) and not(1100 <= n <= 1108):
			# postcode not in Amsterdam ranges
			raise forms.ValidationError('Voer een Amsterdamse postcode in.')
		return value

# Forms		
class SubjectForm(forms.ModelForm):
	woonadres_postcode = AmsterdamPostcodeField()
	correspondentie_postcode = DutchPostcodeField()
	
	class Meta:
		model = Subject