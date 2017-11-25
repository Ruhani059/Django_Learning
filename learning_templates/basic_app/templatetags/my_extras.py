from django import template

register = template.Library()

@register.filter(name='cutt')
def cuttt(value,arg):
    '''
    this cuts out all values of arg from the string!
    '''
    return value.replace(arg,'')

# register.filter('cutt',cuttt)
