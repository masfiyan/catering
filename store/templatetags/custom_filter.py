from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return str(number) + " Rs"



@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

@register.filter(name='divide')
def divide(number , number1):
    return int(number / number1)