
# Django & Compass gebruiken als een User Interaction Design tool

* By: Berry Groenendijk
* Date: 25 february 2010

## Language

This demo is targeted at a Dutch audience. So I will switch to Dutch. Now.

## Licentie/License

**TODO** - licentiemodel bepalen. Vooralsnog ligt het copyright volledig bij de auteur en eigenaar van deze github repository.

## Doel

Ik gebruik al een tijdlang Django en heb sinds kort Compass ontdekt. Compass is een stylesheet authoring framework. En toen realiseerde ik mij het volgende. Django & Compass vormen tezamen een geweldige tool voor het ontwerpen van website schermen (User Interaction Design).

In plaats van papieren ontwerpen, zg. wireframes, Photoshop plaatjes of Firework plaatjes, kun je een compleet functionele en dus klikbare website maken met behulp van Django. En met behulp van Compass kun de site heel snel vormgeven.

Het voordeel van een klikbare, functionele site is dat je daarmee gemakkelijker kan communiceren met eindgebruikers en bijvoorbeeld usability studies kan uitvoeren.

Voor veel eindgebruikers is conceptueel denken heel lastig. En toch vragen we van gebruikers omdat te doen en vragen we zelfs wat er ontbreekt aan het concept en wat er beter aan kan. Het is niet gek dat we dan niet de juiste dingen te horen krijgen.

Bouw snel, continu, release vaak en laat je gebruiker vaak naar het resultaat kijken. En wees niet bang om dingen weg te gooien en opnieuw te doen. Je gooit veel gemakkelijker iets weg waar je slechts weinig tijd aan hebt besteedt dan wanneer je er dagen of weken mee bezig bent geweest.

Met deze demo hoop ik aan te geven dat het maken van een functioneel werkende schets van een website evenveel tijd kost als het maken van een traditioneel wireframe of statisch plaatje. Met als voordeel dat je op deze schets gewoon kunt voortborduren en de site kan uitbouwen tot een productierijpe website.

## Iteratief ontwikkelen

Ik zie Django + Compass ook vooral als een manier om iteratief te ontwikkelen. Op het internet wordt regelmatig aan de hand van een plaatje van de Mona Lisa toegelicht wat het [verschil is tussen incrementeel en iteratief ontwikkelen](http://www.agileproductdesign.com/blog/dont_know_what_i_want.html).

In deze demo gaan we op basis van een probleemstelling ideeën en concepten uitwerken tot een eerste schets van een website. Maar, wel een werkende functionele, klikbare en zelfs testbare schets.

Vanaf dat punt kun je telkens onderdelen van deze schets verder uitwerken en verbeteren. Op die manier wordt de website iteratief steeds beter.

Uiteindelijk kun je de website, gebruikmakend van dezelfde technologie als waar je de schets mee gemaakt hebt, uitbouwen tot een volwaardige, productierijpe website die gebruikt kan worden door tientallen bezoekers maar ook 10-duizenden bezoekers.

## Benodigdheden

Je hebt de volgende software nodig.

*	[Python 2.5](http://python.org/), reeds aanwezig op Mac OS X, Linux, etc. Op Windows dien je het nog te installeren.

*	[Django](http://www.djangoproject.com/download/). Ik heb voor de demo Django 1.1.1 gebruikt. Ik heb Django-1.1.1 uitgepakt en de directory Django-1.1.1 in mijn eigen homedirectory "/Users/berry" geplaatst.

* [Compass](http://wiki.github.com/chriseppstein/compass/getting-started). Voor Compass hebben we Ruby nodig. Op Mac OS X staat Ruby al. Vanaf de command prompt voer de volgende commando's uit:

	sudo gem update --system
	sudo gem install compass

* Als database gebruiken we SQLite. En SQLite wordt meegeleverd met Python 2.5. Dus dat is ook al op de computer aanwezig.

Dat is alles om aan de slag te kunnen.

## Wat gaan we bouwen?

Bij met name Nederlandse gemeenten wordt [zaakgericht werken](http://www.zaakgerichtwerken.nl/) gepropageerd. Wat is het? Burgers vragen bij hun gemeente allerlei zaken aan. Zoals bijv. een vergunning. De gemeente voert hiervoor een aantal handelingen uit. Die hoeveelheid werk wordt een zaak genoemd. Iedere zaak kent een aantal stappen en statussen. Verschillende soorten zaken kunnen verschillende statussen en stappen hebben.

We gaan een website bouwen die gebruikt wordt door ambtenaren om zaken mee af te handelen. Het domein kent globaal de volgende objecten:

* subject, een cliënt die iets aanvragen bij de gemeente
* zaak, een hoeveelheid werk die middels stappen en statussen af te handelen is en te volgen is.
* verstrekking, het product dat geleverd wordt aan de cliënt (bijv. een vergunning of een vergoeding)

Voor onze eerste schets is dit voldoende informatie.

## We beginnen!

Ik heb Django op een willekeurige plek op mijn harde schijf gezet. Ik heb Django in mijn home directory gezet. Even controleren of alles werkt.

	berry$ export PYTHONPATH="/Users/berry/Django-1.1.1/"
	berry$ python
	Python 2.5.1 (r251:54863, Feb  6 2009, 19:02:12) 
	[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import django
	>>> django.VERSION
	(1, 1, 1, 'final', 0)
	>>> 

Gebruik CTRL+D om uit de Python prompt te komen. OK. We are ready to go.

Ga naar je home directory en op je command prompt tik:

	berry$ ./Django-1.1.1/django/bin/django-admin.py startproject djangodemo
	berry$ cd djangodemo/
	berry$ ls
	__init__.py	manage.py	 settings.py	urls.py

De projectdirectory is aangemaakt en een aantal standaard bestanden zijn aangemaakt. Het wordt zometeen duidelijk wat ze betekenen.

Laten we eens kijken wat we gemaakt hebben. Vanuit de djangodemo directory tik:

	python manage.py runserver

Browse naar http://127.0.0.1:8000/ en als het goed is zie je een Django welkom pagina met "It worked!". Deze server is absoluut niet bedoeld voor productie doeleinden, maar voor te ontwikkelen is ie prima.

Eerst nog wat initiële settings aanpassen. Het configuratie bestand van Django is geen XML bestand of iets dergelijks maar gewoon een Python bestand. Heel gemakkelijk. Open het bestand settings.py. Wijzig de volgende variabelen naar:

	DATABASE_ENGINE = 'django.db.backends.sqlite3'
	DATABASE_NAME = '/Users/berry/djangodemo/djangodemo_db' #pas dit aan naar een plek op je eigen harde schijf

Open een nieuwe command prompt en ga naar de djangodemo directory. Op deze manier blijft de server gewoon draaien. Het mooie is dat deze developmentserver wijzigingen in de bestanden gewoon automatisch oppikt. Je hoeft de server niet te herstarten bij iedere wijziging. In de djangodemo directory tik:

	python manage.py syncdb

Resultaat:

	berry$ python manage.py syncdb
	Creating table auth_permission
	Creating table auth_group
	Creating table auth_user
	Creating table auth_message
	Creating table django_content_type
	Creating table django_session
	Creating table django_site
	
	You just installed Django's auth system, which means you don't have any superusers defined.
	Would you like to create one now? (yes/no): yes
	Username (Leave blank to use 'berry'): berry
	E-mail address: berry.groenendijk@gmail.com
	Password: 
	Password (again): 
	Superuser created successfully.
	Installing index for auth.Permission model
	Installing index for auth.Message model

We hebben nu een database aangemaakt en een aantal standaard tabellen zijn aangemaakt.

## Subjecten

We gaan onze eerste Django app maken en wel voor subjecten, de cliënten van een gemeente. Vanuit de djangodemo directory tik:

	berry$ python manage.py startapp subjecten
	berry$ ls
	__init__.py	djangodemo_db	settings.py	 subjecten	urls.pyc
	__init__.pyc	manage.py	settings.pyc	urls.py
	berry$ cd subjecten/
	berry$ ls
	__init__.py	models.py	views.py

Er is een subjecten directory aangemaakt. Het bestand models.py bevat het datamodel van de applicatie. Open het bestand models.py en tik het volgende in:

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

Dit model is niet compleet en de decompositie is niet goed. Maar, dat doet er op dit moment niet toe. We zijn nog alleen maar aan het schetsen. We verzamelen de gegevens die opgeslagen moeten worden bij de business en brengen die onder in een model.

We voegen de applicatie subjecten toe aan de settings.py file dusdanig dat INSTALLED_APPS er als volgt uit ziet:

	INSTALLED_APPS = (
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.sites',
		'djangodemo.subjecten',
	)

Van het model dienen sql statements gemaakt te worden en op de database toegepast te worden. Dat kan met het volgende commando:

	python manage.py syncdb
	
Zou het niet handig zijn om nu te kijken hoe de database eruit ziet en dat we alvast wat data kunnen invullen? Dat gaan we nu dan ook doen.

Django kent een app genaamd Admin. Hiermee kun je de database beheren. We dienen de admin app toe te voegen aan de lijst van apps in de settings.py. Open settings.py en zorg er voor dat INSTALLED_APPS er als volgt uit ziet:

	INSTALLED_APPS = (
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.sites',
		'django.contrib.admin',
		'djangodemo.subjecten',
	)

Synchroniseer opnieuw de modellen met de database:

	python manage.py syncdb

En als laatste dienen we de admin app aan de urls.py toe te voegen. Urls.py bevat het url schema van je applicatie. Het url schema is feite een koppeling tussen een url en de code die de html gaat genereren. Daarover later meer. Haal het commentaar teken, #, weg bij de aangegeven regels in het urls.py bestand zodat het er als volgt uit ziet:

	from django.conf.urls.defaults import *
	
	# Uncomment the next two lines to enable the admin:
	from django.contrib import admin
	admin.autodiscover()
	
		urlpatterns = patterns('',
			# Example:
			# (r'^djangodemo/', include('djangodemo.foo.urls')),
		
			# Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
			# to INSTALLED_APPS to enable admin documentation:
			#(r'^admin/doc/', include('django.contrib.admindocs.urls')),
		
			# Uncomment the next line to enable the admin:
			(r'^admin/', include(admin.site.urls)),
		)

Browse naar http://127.0.0.1:8000/admin. Je krijgt nu een login venster te zien voor het admin scherm. Je ziet een aantal tabellen, maar nog niet de tabellen van subjecten. Dat gaan we veranderen. Maak een bestand admin.py in de subjecten directory

	touch subjecten/admin.py
	edit subjecten/admin.py

Zorg dat subjecten/admin.py er als volgt uit ziet:

	from djangodemo.subjecten.models import Subject
	from django.contrib import admin
	
	admin.site.register(Subject)

Browse naar http://127.0.0.1/admin. Als je nu de tabel subjecten nog niet ziet, herstart dan even de ontwikkelserver. De ontwikkelserver herkent niet automatisch nieuwe bestanden. Je kan ook eventueel het volgende commando uitvoeren:

	touch settings.py

Onder het kopje subjecten staat de tabel subjects genoemd. Hmmm, subjects is in het Nederland niet het meervoud van subject. Dat gaan we veranderen. Wijzig subjecten/models.py naar:

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
		
		class Meta:
			verbose_name_plural = "subjecten"

In de innerclass Meta voegen we een attribuut verbose_name_plural toe. Hierin geven we aan wat de meervouds vorm van de class name is. Bekijk de admin opnieuw en je ziet dat de tabelnaam gewijzigd is. In de admin kunnen we nu simpel data toevoegen aan de tabel subjecten. Voeg twee subjecten in. Verzin simpelweg wat data.

Er vallen een aantal dingen op. Alle velden zijn verplicht. Dit is aan te passen, maar dat doen we later. Ieder object heet "Subject object". Dat laatste gaan we veranderen want dat ziet er vervelend uit. Wijzig subjecten/models.py naar:

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
		
		class Meta:
			verbose_name_plural = "subjecten"
			
		def __unicode__(self):
			return "%s %s %s" % (self.voorletters, self.tussenvoegsels, self.achternaam)

De `__unicode__` functie wordt aangeroepen als de print functie van de class wordt aangeroepen. In de admin verschijnen nu de namen van de subjecten. Mooi zo.

Even terugkijken. We hebben een datamodel aangemaakt, de admin interface geactiveerd en wat data ingevoerd. Netjes. Laten we nu een heuse echt pagina gaan maken voor de website.

## Onze eerste webpagina

Webpagina's in Django worden gegenereerd door views. Een view is een type webpagina. In een view wordt data bij elkaar verzameld om op de webpagina te tonen. In een view wordt ook een template gedefinieerd. Data en template leiden tot een HTML pagina. Maar, je kan net zo goed ook XML, JSON, ASCII, etc. gegenereerd.

Views worden gekoppeld aan een url via de urls.py. In urls.py ontwerp je de urls van de website. In Django ben je geheel vrij in het ontwerpen van de urls van je applicatie.

Laten we eerst het url schema ontwerpen voor onze subjecten. Open subjecten/urls.py:

	berry$ touch subjecten/urls.py
	berry$ edit subjecten/urls.py

En laat het als volgt uit zien:

	from django.conf.urls.defaults import *

	urlpatterns = patterns('djangodemo.subjecten.views',
		(r'^$', 'index'),
		(r'^(?P<subject_id>\d+)/$', 'detail'),
	)

In de hoofddirectory van de djangodemo staat de hoofd urls.py. Daar zullen we nog een verwijzing moeten maken naar de urls.py van subjecten. Open urls.py en laat het als volgt uit zien:

	from django.conf.urls.defaults import *
	
	# Uncomment the next two lines to enable the admin:
	from django.contrib import admin
	admin.autodiscover()
	
	urlpatterns = patterns('',
		# Example:
		# (r'^djangodemo/', include('djangodemo.foo.urls')),
	
		# Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
		# to INSTALLED_APPS to enable admin documentation:
		# (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
		# Uncomment the next line to enable the admin:
		(r'^admin/', include(admin.site.urls)),
		
		# Subjecten
		(r'^subjecten/', include("djangodemo.subjecten.urls")),
	)

Het leidt er toe dat de url `/subjecten` de methode index in djangodemo.subjecten.view aanroept. En dat bijvoorbeeld de url `/subjecten/10` de methode detail aanroept in de djangodemo.subjecten.views met de parameter 'subject_id' die in dit geval de waarde '10' heeft. 

Open het bestand subjecten/views.py en laat het er als volgt uit zien:

	from django.shortcuts import render_to_response
	
	from djangodemo.subjecten.models import Subject
	
	def index(request):
		'''Lijst van alle subjecten'''
	
		subjecten = Subject.objects.all()
		return render_to_response('subjecten/index.html', {'subjecten': subjecten})
		
	def detail(request, subject_id):
		'''Details van een subject'''
	
		subject = Subject.objects.get(pk = subject_id)
		return render_to_response('subjecten/detail.html', {'subject': subject})

`render_to_response` is een hulpfunctie om snel een template plus een data dictionary samen te voegen en terug te geven aan de HTTP response.

Als je nu naar http://127.0.0.1:8000/subjecten gaat dan zie je een foutmelding dat Django het template bestand niet kan vinden. De locatie van de templates staat in settings.py in de variabele `TEMPLATE_DIRS`. Open settings.py en wijzig `TEMPLATE_DIRS`in:

	TEMPLATE_DIRS = (
		# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
		# Always use forward slashes, even on Windows.
		# Don't forget to use absolute paths, not relative paths.
		"/Users/berry/git/djangodemo/templates",
	)

Maak het bestand templates/subjecten/index.html:

	mkdir templates
	mkdir templates/subjecten
	touch templates/subjecten/index.html

Laat templates/subjecten/index.html er als volgt uit zien:

	{% block content %}
		<h2>Lijst van cliënten</h2>
		<table>
			<tr>
				<th>Naam</th>
				<th>Woonplaats</th>
			</tr>
			{% for subject in subjecten %}
			<tr>
				<td><a href="/subjecten/{{ subject.id }}">{{ subject.voorletters }} {{ subject.tussenvoegsels }} {{ subject.achternaam }}</a></td>
				<td>{{ subject.woonadres_woonplaats|upper }}</td>
			</tr>
			{% endfor %}
		</table>
	{% endblock content %}
	
Browse naar http://127.0.0.1:8000/subjecten en voila onze eerste webpagina!

En hier komt de grote kracht van Django naar voren. Als webdesigner ben je volledig vrij in het maken van de HTML. De template taal van Django is heel eenvoudig en door webdesigners te begrijpen. Een template kan dus gemaakt worden door een webdesigner. Daar hoeft geen programmeur aan te pas te komen. In de template taal wordt geen Python gebruikt. Je kunt als programmeur dan ook niet verleidt worden om te programmeren in de template. Code en HTML template zijn strict van elkaar gescheiden.

De `{% %}` tags zijn stuur commando's zoals simpele for-loops of if-then constructies. De `{{ }}` tags zijn placeholders voor data. De template wordt gevoed met een data dictionary (zie ook de methode index eerder in het views.py bestand). In de data tags kun je 1 of meerdere filters gebruiken om de data op te maken. Bij woonplaats heb ik het filter upper gebruikt die de woonplaats in bovenkast plaatst.

Maak het bestand templates/subjecten/detail.html:

	touch templates/subjecten/detail.html

Open dit bestand en laat het als volgt uit zien:

	{% block content %}
		<h2>Cliëntgegevens van {{ subject.voorletters }} {{ subject.tussenvoegsels }} {{ subject.achternaam }}</h2>
		<table>
			<tr>
				<th>Woonadres</th>
				<th>Correspondentieadres</th>
			</tr>
			<tr>
				<td>{{ subject.voorletters }} {{ subject.tussenvoegsels }} {{ subject.achternaam }}<br/>
				{{ subject.woonadres_straatnaam }} {{ subject.woonadres_huisnummer }} {{ subject.woonadres_huisnummer_toevoeging }}<br/>
				{{ subject.woonadres_postcode|upper }}&nbsp;&nbsp;{{ subject.woonadres_woonplaats|upper }}
				</td>
				<td>{{ subject.voorletters }} {{ subject.tussenvoegsels }} {{ subject.achternaam }}<br/>
				{{ subject.correspondentie_straatnaam }} {{ subject.correspondentie_huisnummer }} {{ subject.correspondentie_huisnummer_toevoeging }}<br/>
				{{ subject.correspondentie_postcode|upper }}&nbsp;&nbsp;{{ subject.correspondentie_woonplaats|upper }}
				</td>
			</tr>
		</table>
	{% endblock content %}

Dit is wel een hele eenvoudige weergave van een client. Maar goed, we zijn nog steeds aan het schetsen. We kunnen nu in de lijst van clienten klikken op een client en krijgen dan de details van de client te zien. De eerste contouren van een functionele en klikbare website ontstaan.

We gaan nu nog een stukje van de kracht van Django templates zien: inheritance van templates.

Maak het bestand templates/subjecten/base.html. Dit bestand gaat de basis html bevatten, laat het als volgt uit zien:

	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
		"http://www.w3.org/TR/html4/strict.dtd"> 
	<html>
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
			<title>Demo Django & Compass</title>
		</head>
		<body>
			<div id="header">
				<h1>Demo Django & Compass</h1>
			</div>
			<div id="menu">
				<ul>
					<li><a href="/subjecten">Cliënten</a></li>
				</ul>
			</div>
			<div id="content">
				{% block content %}
					<p>-</p>
				{% endblock %}
			</div>
			<div id="footer"> 
				<ul> 
					<li><a href="/">Home</a></li> 
					<li><a href="#">About</a></li> 
					<li><a href="#">Contact</a></li> 
					<li>&copy;</li> 
				</ul> 
			</div> 
		</body>
	</html>

Wees er zeker van dat je het bestand als UTF-8 opslaat.

We hebben een nette HTML basis template met daarin een header block, een menu block, een content block en een footer block. Het content block heb ik ook voorzien van een Django template block aanduiding.

Wijzig templates/subjecten/index.html en templates/subjecten/details.html en zet op de allereerste regel van deze twee bestanden:

	{% extends "base.html" %}

Als je naar de subjecten pagina browsed dan zie je een complete HTML pagina met een titel, een menu en een footer.

Wat we nog missen is een begin pagina voor onze site. Maak het bestand templates/index.html aan en laat het als volgt uit zien:

	{% extends "base.html" %}
	
	{% block content %}
		<p>Welkom bij deze demo van Django & Compass waarin we proberen aan te tonen 
		dat deze combinatie een heel mooie User Interaction Design tool kan zijn.</p>
	{% endblock content %}

Echter, we hebben nog geen url en nog geen view gedefinieerd. Dat gaan we dus ook even doen. Urls.py komt er als volgt uit te zien:

	from django.conf.urls.defaults import *
	
	# Uncomment the next two lines to enable the admin:
	from django.contrib import admin
	admin.autodiscover()
	
	urlpatterns = patterns("django.views.generic.simple",
		
		# Hoofdpagina's
		(r'^$', "direct_to_template", {'template': 'index.html'}),
	)
	
	urlpatterns = urlpatterns + patterns('',
		# Example:
		# (r'^djangodemo/', include('djangodemo.foo.urls')),
	
		# Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
		# to INSTALLED_APPS to enable admin documentation:
		# (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
		# Uncomment the next line to enable the admin:
		(r'^admin/', include(admin.site.urls)),
		
		# Subjecten
		(r'^subjecten/', include("djangodemo.subjecten.urls")),
	)

We gebruiken hier een generic view genaamd `direct_to_template` waarmee je snel views in elkaar kan zetten. Er zijn meer generic views. O.a. een master-detail view. Die zullen we later gebruiken.

We hebben nu een compleet werkende website! Alleen hij ziet er nog niet uit. Dat gaan we nu doen. We gaan de site opmaken.

## De site vormgeven met behulp van Compass

Voer de volgende commando's vanuit de hoofddirectory van het djangodemo project:

	mkdir static
	mkdir static/css
	cd static/css
	compass -f blueprint djangodemo

We maken gebruik van het blueprint CSS framework. Compass maakt nu een hele serie directories en bestanden aan. Ook geeft Compass nu aanwijzingen om de CSS in je HTML te linken. Neem deze aanwijzingen over in het base.html bestand, de head van base.html ziet er nu als volgt uit:

	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
		<title>Demo Django & Compass</title>
		<link href="/static/css/djangodemo/stylesheets/screen.css" media="screen, projection" rel="stylesheet" type="text/css" />
		<link href="/static/css/djangodemo/stylesheets/print.css" media="print" rel="stylesheet" type="text/css" />
		<!--[if lt IE 8]>
			<link href="/static/css/djangodemo/stylesheets/ie.css" media="screen, projection" rel="stylesheet" type="text/css" />
		<![endif]-->
	</head>
	
Als we kijken of de CSS wordt opgepikt dan blijkt dat niet zo te zijn. De url naar de static directory wordt nog niet opgepikt. Dat moeten we even rechttrekken. Open urls.py en wijzig deze in:

	from django.conf.urls.defaults import *
	
	# Uncomment the next two lines to enable the admin:
	from django.contrib import admin
	admin.autodiscover()
	
	urlpatterns = patterns("django.views.generic.simple",
		
		# Hoofdpagina's
		(r'^$', "direct_to_template", {'template': 'index.html'}),
	)
	
	urlpatterns = urlpatterns + patterns('',
		# Example:
		# (r'^djangodemo/', include('djangodemo.foo.urls')),
	
		# Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
		# to INSTALLED_APPS to enable admin documentation:
		# (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
		# Uncomment the next line to enable the admin:
		(r'^admin/', include(admin.site.urls)),
		
		# Subjecten
		(r'^subjecten/', include("djangodemo.subjecten.urls")),
		
		# Static media
		# ONLY USE THIS FOR THE DEVELOPMENT SERVER. NEVER USE THIS IN PRODUCTION.
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/berry/git/djangodemo/static'}),
	)

Onder aan het bestand heb we een regel toegevoegd waarmee de statische media in de directory `/Users/berry/git/djangodemo/static` worden geserveerd door de development server. Als je nu een pagina bekijkt dan zie je dat de CSS netjs wordt opgepikt. De layout is iets gewijzigd t.o.v. van eerst.

Nu gaan kunnen we de site gaan stijlen.

Open een command prompt en ga naar de directory `/Users/berry/git/djangodemo/static/css/djangodemo`. Dit is de directory waar het Compass project is aangemaakt. We laten Compass deze directory bewaken, zodat iedere wijziging meteen wordt gecompileerd tot CSS bestanden:

	compass -w

We gaan nu in de subdirectory stylesheets van het Compass project het bestand screen.sass aanpassen. Sass is een meta-taal waarmee je makkelijker, overzichtelijker en met meer kracht CSS kan schrijven. Vooral het gebruik van import, variabelen en mixins maakt Sass heel krachtig. Je kunt nu heel modulair te werk gaan in CSS. Compass zorgt er voor jou voor dat een en ander weer naar CSS wordt omgevormd. Deze techniek scheelt echt enorm veel tijd bij het maken en onderhouden van CSS. 

Screen.sass ziet er nu als volgt uit:

	// This import applies a global reset to any page that imports this stylesheet.
	@import blueprint/reset.sass
	// To configure blueprint, edit the partials/base.sass file.
	@import partials/base.sass
	// Import all the default blueprint modules so that we can access their mixins.
	@import blueprint
	// Import compass utilities
	@import compass/utilities.sass
	
	// djangodemo layout
	+blueprint-typography("body")
	body
	  +container
	  !sidebar_columns = floor(!blueprint_grid_columns / 4)
	  #menu
		+column(!sidebar_columns)
		+no-bullets
	  #content
		+column(!blueprint_grid_columns - !sidebar_columns, true)
	  #footer, #header
		+column(!blueprint_grid_columns)
	  #footer
		background-color = #eee
		margin-top = 1em
		+horizontal-list(5px)
		
	table
	  +table-scaffolding
	  th
		background-color = #eee
		text-align = "left"

De website ziet er nu eenvoudig met wel gestyled uit. We maken hier gebruik van het Blueprint CSS framework. Dit framework biedt een mooi grid waarmee je een webpagina strak kan indelen in functionele kolommen en blokken.

Compass biedt ook een aantal handige mixins waarmee je bijv. een unordered-list gemakkelijk horizontaal kan weergeven. Zoals we in de footer hebben gedaan.

Bug: op mijn laptop staat de titel op de homepage helemaal bovenaan, terwijl die op alle andere pagina's netjes ruimte heeft bovenaan. Geen idee waarom dat dit is. Ik ben dan ook geen HTML-CSS expert. [28 feb 2010: bug opgelost. De index.html pagina in de hoofddirectory van het project was opgeslagen als UTF-8 zonder BOM, terwijl alle andere pagina's in UTF-8 met BOM waren opgeslagen. Index.html ook in UTF-8 met BOM opgeslagen en toen zag de startpagina er wel goed uit.]

## Even terugkijken...

We hebben nu een complete, functionele, werkende en klikbare website die ook nog eens (eenvoudig) gestyled is. Plus dat we een admin interface hebben waarmee we onze tabellen kunnen vullen en onderhouden.

Dit vormt het einde van onze eerste iteratie. Een ruwe schets van onze Mona Lisa is uitgewerkt. We kunnen deze schets nu al aan onze klant of eindgebruikers laten zien.

Sterker nog onze eindgebruikers zouden nu al mee aan het werk kunnen gaan met de website. Bijv. door de cliënten database te gaan vullen. Hoewel de website zelf nog maar erg weinig functionaliteit biedt. Maar, als eindgebruiker zou men nu al iets kunnen gaan zeggen over de layout of bijv. de gegevens die men mist bij een cliënt. En dat al na een klein uurtje werk. Moet je nagaan wat je na een dag werken in overleg met je eindgebruikers al bereikt zou kunnen hebben.

Plus dat deze versie van de website de basis vormt voor de rest van onze ontwikkelingen.

Hieronder volgen, minder uitgebreidt, nog de nodige Django en Compass tips en notities over de uitbreidingen en wijzigingen op deze demo. De resultaten hiervan zijn in [Github](http://github.com/berry/Django-demo) terug te vinden. Bekijk vooral deze source code, lees het en leer ervan.

Onderaan dit document vindt je ook een aantal referenties en links naar websites met meer informatie over Django, Compass, etc.

## CSS Debug grid

In Blueprint kun je ook een debug grid aanzetten. Dit grid geeft je visuele aanwijzingen over de verdeling van de content over de kolommen van het grid.

Wijzig de urls.py in de hoofddirectory van het project naar:

	from django.conf.urls.defaults import *
	
	# Uncomment the next two lines to enable the admin:
	from django.contrib import admin
	admin.autodiscover()
	
	urlpatterns = patterns("django.views.generic.simple",
		
		# Hoofdpagina's
		(r'^$', "direct_to_template", {'template': 'index.html'}),
	)
	
	urlpatterns = urlpatterns + patterns('',
		# Example:
		# (r'^djangodemo/', include('djangodemo.foo.urls')),
	
		# Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
		# to INSTALLED_APPS to enable admin documentation:
		# (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
		# Uncomment the next line to enable the admin:
		(r'^admin/', include(admin.site.urls)),
		
		# Subjecten
		(r'^subjecten/', include("djangodemo.subjecten.urls")),
		
		# Static media
		# ONLY USE THIS FOR THE DEVELOPMENT SERVER. NEVER USE THIS IN PRODUCTION.
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/berry/git/djangodemo/static'}),
		(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/berry/git/djangodemo/static/images'}),    
	)

We hebben een url pad toegevoegd voor images. We dienen de directory waarnaar verwezen wordt ook aan te maken. Vanuit de hoofddirectory van het project voer uit:

	mkdir static/images
	cp static/css/djangodemo/images/* ./static/images/
	
We hebben ook de plaatjes van de Compass directory naar de static/images gekopieerd.

Nu kunnen we in de .sass bestanden +blueprint-debug en +showgrid toevoegen aan het bestand screen.sass:

	// This import applies a global reset to any page that imports this stylesheet.
	@import blueprint/reset.sass
	// To configure blueprint, edit the partials/base.sass file.
	@import partials/base.sass
	// Import all the default blueprint modules so that we can access their mixins.
	@import blueprint
	// Import compass utilities
	@import compass/utilities.sass
	
	// djangodemo layout
	+blueprint-typography("body")
	+blueprint-debug
	body
	  // Uncomment next line to make the debug grid visible
	  //+showgrid
	  +container
	  !sidebar_columns = floor(!blueprint_grid_columns / 4)
	  #menu
		+column(!sidebar_columns)
		+no-bullets
	  #content
		+column(!blueprint_grid_columns - !sidebar_columns, true)
	  #footer, #header
		+column(!blueprint_grid_columns)
	  #footer
		background-color = #eee
		margin-top = 1em
		+horizontal-list(5px)
		
	table
	  +table-scaffolding
	  th
		background-color = #eee
		text-align = "left"

Het +showgrid commando kun je nu aan en uitzetten. Zet je +showgrid aan dan wordt op de website een plaatje getoond met daarin de kolommen aangegeven.

## Referenties

* De [Django tutorial](http://docs.djangoproject.com/en/dev/intro/tutorial01/) is een zeer goede introductie in het gebruik van Django. Deze demo volgt grotendeels ook deze introductie. De introductie legt op onderdelen echter iets meer uit. Ik heb slechts een introductie op de introductie gegeven.

* De grote kracht van Django is de [documentatie](http://docs.djangoproject.com/en/1.1/). Algemeen wordt erkend dat deze documentatie zeer goed geschreven is en mede de basis vormt voor het succes van Django. Je vindt heel gemakkelijk dingen terug en je leert dan ook heel snel meer van Django.

* Voor het gebruik van [Compass](http://wiki.github.com/chriseppstein/compass/) is een screencast gemaakt. Deze is informatief maar duurt wel wat lang (50 minuten). Het laat wel zien hoe krachtig Compass is.

* Compass bouwt voort op [Sass](http://sass-lang.com/about.html).

* Deze [Django demo](http://github.com/berry/Django-demo) heb ik op Github geplaatst. Github is gratis voor open source projecten en biedt een geweldige webinterface op [Git](http://git-scm.com/).

* Django is geschreven in [Python](http://python.org/). Python is een krachtige dynamische programmeertaal. Ontstaan bij het [CWI](http://www.cwi.nl/) in Amsterdam en geschreven door [Guido van Rossum](http://www.python.org/~guido/). Python kent een (zeer) grote schare aanhangers en wordt door zeer vele organisaties gebruikt. Python leren is gemakkelijk. In zeer korte tijd ben je als programmeur als heel effectief bezig met het maken van functionele programma's. Python kent, zeker in tegenstelling tot Java, maar weinig boeken. Dat is geen indicatie dat Python weinig gebruikt wordt, maar een indicatie van de eenvoud van de taal. 

* Compass en Sass zijn geschreven in [Ruby](http://www.ruby-lang.org/en/). Ruby heeft dynamische programmeertalen enorm populair gemaakt. Python en Ruby worden heel vaak als elkaars concurrenten gezien. Maar, er is ruimte genoeg voor beide talen.