from django import template

register = template.Library()

@register.filter(name="first_letter")
def first_letter(mineral):
    """returns first letter of passed in mineral name as lowercase"""
    return mineral.name[0].lower()