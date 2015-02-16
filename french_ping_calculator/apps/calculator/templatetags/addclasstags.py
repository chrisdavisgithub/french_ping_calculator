from django import template
register = template.Library()


@register.filter(name='addclass')
def addclass(field, value):
    return field.as_widget(attrs={"class": value})
