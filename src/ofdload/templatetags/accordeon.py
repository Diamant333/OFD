from django import template
import inflect
register = template.Library()


@register.simple_tag
def convert(val=None):
    p = inflect.engine()
    p = p.number_to_words(val)
    p = p.capitalize()
    return p
