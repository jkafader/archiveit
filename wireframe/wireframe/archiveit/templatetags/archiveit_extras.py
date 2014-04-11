from django.core import serializers
from django import template

register = template.Library()

def jsonize(object):
    return serializers.serialize("json", object)

register.filter("jsonize", jsonize)