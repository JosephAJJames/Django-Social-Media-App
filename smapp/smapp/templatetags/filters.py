from django import template

register = template.Library()

@register.filter
def get_value(dictionary, key):
    if dictionary is not None and key is not None:
        return dictionary.get(key)
    return []

@register.filter
def add_class(field ,css_class):
    if hasattr(field, 'as_widget'):  # Check if it's a form field
        return field.as_widget(attrs={'class': css_class})
    elif hasattr(field, 'label'):  # Check if it's a label (simple case)
        return f'<label class="{css_class}">{field.label}</label>'
    return field  # Return the original if neither case matches
