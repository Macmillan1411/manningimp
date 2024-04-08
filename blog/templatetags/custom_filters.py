from django import template

register = template.Library()

@register.filter
def split_by_newline(text):
    return text.split('\n')
