# template tags and filters
import datetime

from django import template

register = template.Library()

def leeftijd(value):
	return (datetime.datetime.now().date() - value).days/365
	
register.filter('leeftijd', leeftijd)