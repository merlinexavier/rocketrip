from django import template
from datetime import date

register = template.Library()


@register.filter(name='elapsed_days')
def elapsed_days(value):
    elapsed = 0
    try:
        elapsed = (date.today() - value).days
    except:
        elapsed = 'unknown'
    return elapsed
