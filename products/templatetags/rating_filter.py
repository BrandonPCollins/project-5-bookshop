from django import template

register = template.Library()

@register.filter
def is_gte(user_rating, star_value):
    return user_rating >= star_value