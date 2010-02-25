# Django & Compass gebruiken als een User Interaction Design tool

By: Berry Groenendijk

Date: 25 february 2010

## Language

This demo is targeted at a Dutch audience. So I will switch to Dutch. Now.

## Doel

Ik gebruik al een tijdlang Django en heb sinds kort Compass ontdekt. Compass is een stylesheet authoring framework. En toen vroeg ik mij het volgende af. Django & Compass vormen tezamen een geweldige tool voor het ontwerpen van website schermen (User Interaction Design).

In plaats van papieren ontwerpen, zg. wireframes, Photoshop plaatjes of Firework plaatjes, kun je een compleet functionele en dus klikbare website maken met behulp van Django. En met behulp van Compass kun de site heel snel vormgeven.

Ik denk dat je zo'n website in evenveel tijd kan bouwen als een traditionele wireframe. Ook beweer ik dat zo'n website net zo aanpasbaar is.

## Benodigdheden

Je hebt de volgende software nodig.

*	[Python](http://python.org/), reeds aanwezig op Mac OS X, Linux, etc. Op Windows dien je het nog te installeren.

*	[Django](http://www.djangoproject.com/download/). Ik heb voor de demo Django 1.1.1 gebruikt. Volg de installatie instructies onder optie 1.

* **TODO** [Compass](http://wiki.github.com/chriseppstein/compass/getting-started) installatie

## Wat gaan we bouwen?

Bij met name Nederlandse gemeenten wordt [zaakgericht werken](http://www.zaakgerichtwerken.nl/) gepropageerd. Wat is het? Burgers vragen bij hun gemeente allerlei zaken aan. Zoals bijv. een vergunning. De gemeente voert hiervoor een aantal handelingen uit. De hoeveelheid werk wordt een zaak genoemd. Iedere zaak kent een aantal stappen en statussen. Iedere soort zaak kunnen verschillende statussen en stappen hebben.

We gaan een website bouwen die gebruikt wordt door ambtenaren om zaken mee af te handelen. Het domein kent globaal de volgende objecten:

* subject, een cli‘nt die iets aanvragen bij de gemeente
* zaak, een hoeveelheid werk die middels stappen en statussen af te handelen is en te volgen is.
* verstrekking, het product dat geleverd wordt aan de cli‘nt (bijv. een vergunning of een vergoeding)

## We beginnen!

**TODO**