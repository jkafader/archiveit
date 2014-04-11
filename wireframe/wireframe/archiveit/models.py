from django.db import models
import jsonfield
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
    owner = models.ForeignKey("accounts.Account", blank=True, null=True)
    public = models.BooleanField(default=False)
    metadata = jsonfield.JSONField()
    active = models.BooleanField(default=True)
    topics = models.ForeignKey('CollectionTopic', blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    last_crawl = models.DateTimeField(blank=True, null=True)
    comments = generic.GenericRelation('Comment')
    def next_crawl_date(self):
        return datetime.now + datetime.timedelta(7)
    def __unicode__(self):
        return "[Collection]".format()
    def save(self, *args, **kwargs):
        #TODO: set owner here.
        if not self.pk:
            self.created_on = datetime.now()
        self.updated_on = datetime.now()
        super(Collection, self).save(*args, **kwargs)

# CollectionTopics exist to 
# They are shared between all users.
class CollectionTopic(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return "[CollectionTopic] {}".format(self.name)

# this function provides the default folder for Seeds
def get_uncategorized_seed_folder():
    return SeedFolder.objects.get_or_create(name='Uncategorized')[0]

# Seeds represent the URL from which a Crawl should commence, as well as a 
# frequency schedule
class Seed(models.Model):
    url = models.URLField(max_length=200)
    collection = models.ForeignKey('Collection')
    owner = models.ForeignKey("accounts.Account", blank=True, null=True)
    frequency = models.CharField(max_length=3, choices=CONSTANTS['SeedFrequency'])
    capture = models.ForeignKey('SeedCapturePattern', blank=True, null=True)
    public = models.BooleanField(default=False)
    login = models.BooleanField(default=False)
    folder = models.ForeignKey('SeedFolder', blank=True, null=True, default=get_uncategorized_seed_folder)
    metadata = jsonfield.JSONField(blank=True, null=True)
    comments = generic.GenericRelation('Comment')
    #def next_crawl_date():
    #    crawl in self.crawl_set.():
            
    def __unicode(self):
        return "[Seed] {}{}{}".format(self.url, self.public and " (public)", self.frequency and " frequency: " + self.frequency)

# SeedCapturePatterns are a list of filetypes patterns for seeds to capture. They're set up as a class so they can be administered through the admin.
class SeedCapturePattern(models.Model):
    name = models.CharField(max_length=100)
    pattern = models.CharField(max_length=200)
    def __unicode__(self):
        return "{} ({})".format(self.name, self.pattern)

# SeedScopeRules define boundaries for Crawls spawned by a Seed.
class SeedScopeRule(models.Model):
    collection = models.ForeignKey('Collection', blank=True, null=True)
    seeds = models.ManyToManyField('Seed', blank=True, null=True)
    rule_type = models.CharField(max_length=20, choices=CONSTANTS['SeedScopeRuleTypes'], blank=True, null=True)
    rule_match = models.CharField(max_length=200, blank=True, null=True)
    document_limit = models.IntegerField(default=10000, blank=True, null=True)
    use_document_limit = models.BooleanField(default=True)
    comments = generic.GenericRelation('Comment')
    def print_rule(self):
        return "{}".format(self.rule_type and " URL " + self.rule_type + " '" + self.rule_match + "'" or "")
    def __unicode__(self):
        return "[SeedScopeRule]{}{}".format(
                   self.rule_type and " URL " + self.rule_type + " " + self.rule_match or "",
                   self.use_document_limit and " limit to " + str(self.document_limit) or "",
               )
    def save(self, *args, **kwargs):
        # save initially, to ensure that we have a primary key when working on the below
        super(SeedScopeRule, self).save(*args, **kwargs)
        # add references to my Collection's Seeds if I have a Collection but no Seeds
        if self.collection and not self.seeds.count():
            self.seeds.add(*[seed for seed in self.collection.seed_set.all()])

# Seed folders are not hierarchical.
class SeedFolder(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey("accounts.Account", blank=True, null=True)
    def __unicode__(self):
        return "[SeedFolder] {}".format(self.name)

# Crawls are created from Seeds, presumably by a cron or Celery like process.
class Crawl(models.Model):
    seed = models.ForeignKey('Seed')
    begun_on = models.DateTimeField()
    ended_on = models.DateTimeField()
    completed = models.BooleanField()
    metadata = jsonfield.JSONField(blank=True, null=True)
    comments = generic.GenericRelation('Comment')
    def __unicdoe__(self):
        #TODO: if self.seed is not strictly necessary here, consider removing it. Triggers a query.
        return "[Crawl] From {} begun {:%Y-%m-%d %H:%i:%s}".format(self.seed, self.begun_on)

# Documents are created by Crawls, after fetching a url.
class Document(models.Model):
    crawl = models.ForeignKey('Crawl')
    body = models.TextField(blank=True, null=True)
    url = models.URLField()
    fetch_date = models.DateTimeField(default=datetime.now)
    metadata = jsonfield.JSONField(blank=True, null=True)
    comments = generic.GenericRelation('Comment')

# Comments can apply to any other object via the 'comment_on' GenericForiegnKey.
class Comment(models.Model):
    comment = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    comment_on = generic.GenericForeignKey()
    def __unicode__(self):
        return "[Comment] on {} #{}".format(self.content_type, self.object_id)
