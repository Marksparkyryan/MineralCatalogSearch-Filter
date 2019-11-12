from django import template

register = template.Library()

GROUPS = ['Silicates', 'Oxides', 'Sulfates', 'Sulfides', 'Carbonates',
          'Halides', 'Sulfosalts', 'Phosphates', 'Borates', 'Organic Minerals',
          'Arsenates', 'Native Elements', 'Other', ]

COLOURS = [
    'Blue', 'Yellow', 'Green', 'Red', 'Orange', 'Pink', 'Purple', 'White',
    'Black', 'Gray', 'Brown', 'Grey', 'Violet', 'Bronze', 'Gold'
]

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


@register.simple_tag
def groups():
    return GROUPS


@register.simple_tag
def colours():
    return COLOURS


@register.simple_tag
def alphabet():
    return ALPHABET
    