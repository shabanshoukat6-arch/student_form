from django import template
register = template.Library()


@register.filter(name='change')
def change(value,args):
    for character in args:
        value = value.replace(character,"")
    return value