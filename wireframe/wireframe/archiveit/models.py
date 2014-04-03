from django.db import models
from picklefield.fields import PickledObjectField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from datetime import datetime

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

# Collections represent 
class Collection(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey("auth.User", blank=True, null=True)
    public = models.BooleanField(default=False)
    metadata = PickledObjectField()
    active = models.BooleanField(default=True)
    topics = models.ForeignKey('CollectionTopic', blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.now)
    updated_on = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return "[Collection]".format()
    def save(self, *args, **kwargs):
        #TODO: set owner here.
        self.updated_on = datetime.now()
        super(Collection, self).save(*args, **kwargs)

# CollectionTopics exist to 
# They are shared between all users.
class CollectionTopic(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return "[CollectionTopic] {}".format(self.name)

# this function provides the default folder for Seeds
#def get_uncategorized_seed_folder():
#    return SeedFolder.objects.get(name='Uncategorized')

# Seeds represent the URL from which a Crawl should commence, as well as a 
# frequency schedule
class Seed(models.Model):
    url = models.URLField(max_length=200)
    collection = models.ForeignKey('Collection')
    frequency = models.CharField(max_length=3, choices=CONSTANTS['SeedFrequency'])
    public = models.BooleanField(default=False)
    folder = models.ForeignKey('SeedFolder', blank=True, null=True, )#default=get_uncategorized_seed_folder)
    group = models.ForeignKey('SeedGroup', blank=True, null=True)
    metadata = PickledObjectField(blank=True, null=True)
    def __unicode(self):
        return "[Seed] {}{}{}".format(self.url, self.public and " (public)", self.frequency and " frequency: " + self.frequency)

# SeedScopeRules define boundaries for Crawls spawned by a Seed.
class SeedScopeRule(models.Model):
    rule_type = models.CharField(max_length=20, choices=CONSTANTS['SeedScopeRuleTypes'])
    rule_match = models.CharField(max_length=200)
    document_limit = models.BooleanField()
    use_document_limit = models.IntegerField()
    def __unicode__(self):
        return "[SeedScopeRule]{}{}".format(
                   self.rule_type and " URL " + self.rule_type + " " + self.rule_match or "",
                   self.use_document_limit and " limit to " + self.document_limit or "",
               )

# TODO: Ask someone why we need SeedGroups in addition to SeedFolders.
class SeedGroup(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return "[SeedGroup] {}".format(self.name)

# Seed folders are a hierarchical tree structure. The 'parent' field makes this happen.
# a [null] in the 'parent' field means that this terminates a folder tree.
class SeedFolder(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    def __unicode__(self):
        return "[SeedFolder] {}".format(self.name)

# Crawls are created from Seeds, presumably by a cron or Celery like process.
class Crawl(models.Model):
    seed = models.ForeignKey('Seed')
    begun_on = models.DateTimeField()
    ended_on = models.DateTimeField()
    completed = models.BooleanField()
    metadata = PickledObjectField(blank=True, null=True)
    def __unicdoe__(self):
        #TODO: if self.seed is not strictly necessary here, consider removing it. Triggers a query.
        return "[Crawl] From {} begun {:%Y-%m-%d %H:%i:%s}".format(self.seed, self.begun_on)

# Documents are created by Crawls, after fetching a url.
class Document(models.Model):
    crawl = models.ForeignKey('Crawl')
    body = models.TextField(blank=True, null=True)
    url = models.URLField()
    fetch_date = models.DateTimeField(default=datetime.now)
    metadata = PickledObjectField(blank=True, null=True)

# Comments can apply to any other object via the 'comment_on' GenericForiegnKey.
class Comment(models.Model):
    comment = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    comment_on = generic.GenericForeignKey()
    def __unicode__(self):
        return "[Comment] on {} #{}".format(self.content_type, self.object_id)
