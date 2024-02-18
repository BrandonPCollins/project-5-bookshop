from django import template

register = template.Library()

@register.filter
def range_filter(value):
    if value is None:
        return range(0)
    return range(int(value))

@register.filter
def subtract(value, arg):
    if arg is None:
        arg = 0
    return value - arg

@register.filter
def to_int(value):
    return int(value)

