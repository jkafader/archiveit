from django.db import models
from picklefield.fields import PickledObjectField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

CONSTANTS = {
    'SeedFrequency': (
       ('0', 'One Time'),
       ('1', 'Daily'),
       ('7', 'Weekly'),
       ('30', 'Monthly'),
       ('365', 'Yearly'),
       ('3650', 'Once per Decade'),
    ),
    'SeedScopeRuleTypes':(
       ('contains', "If the URL contains the following text:"),
       ('startswith', "If the URL starts with the following text:"),
       ('endswith', "If the URL ends with the following text:"),
       ('matches', "If the URL matches the Regular Expression:")
    )
}

# Create your models here.
class UserMessage(models.Model):
    message = models.CharField(max_length=100)

class Collection(models.Model):
    name = models.CharField(max_length=100)
    public = models.BooleanField()
    metadata = PickledObjectField()

class Seed(models.Model):
    url = models.URLField(max_length=200)
    collection = models.ForeignKey('Collection')
    frequency = models.CharField(max_length=3, choices=CONSTANTS['SeedFrequency'])
    public = models.BooleanField()
    group = models.ForeignKey('SeedGroup')
    folder = models.ForeignKey('SeedFolder')

class SeedScopeRule(models.Model):
    rule_type = models.CharField(max_length=20, choices=CONSTANTS['SeedScopeRuleTypes'])
    rule_match = models.CharField(max_length=200)
    document_limit = models.BooleanField()
    use_document_limit = models.IntegerField()

class SeedGroup(models.Model):
    name = models.CharField(max_length=200)

class SeedFolder(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', related_name='children')

class Crawl(models.Model):
    seed = models.ForeignKey('Seed')
    begun_on = models.DateTimeField()
    ended_on = models.DateTimeField()
    completed = models.BooleanField()
    def __unicdoe__(self):
        return ""

class Comment(models.Model):
    comment = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    comment_on = generic.GenericForeignKey()
    def __unicode__(self):
        return self.comment
