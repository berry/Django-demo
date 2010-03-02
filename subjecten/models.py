from django.db import models

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