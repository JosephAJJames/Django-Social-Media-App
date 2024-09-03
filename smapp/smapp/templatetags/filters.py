from django import template

register = template.Library()

@register.filter
def get_value(dictionary, key):
    if dictionary is not None and key is not None:
        return dictionary.get(key)
    return []