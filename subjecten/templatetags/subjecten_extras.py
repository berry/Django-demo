# template tags and filters
import datetime

from django import template

register = template.Library()

def leeftijd(value):
    """
    Calculate the age of a user.
    
    value = datetime.date object for birth day
    """
    today = datetime.date.today()
    try:
		birthday = datetime.date(today.year, value.month, value.day)
    except ValueError:
		# Raised when person was value on 29 February and the current
		# year is not a leap year.
		birthday = datetime.date(today.year, value.month, value.day - 1)
    if birthday > today:
        return today.year - value.year - 1
    else:
        return today.year - value.year
	
register.filter('leeftijd', leeftijd)