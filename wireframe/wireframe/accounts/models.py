from django.db import models
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

CONSTANTS = {
    "StorageUnits":(
        ("MB", "MB"),
        ("GB", "GB"),
        ("TB", "TB"),
        ("PB", "PB"),
        ("EB", "EB"),
    ),
    "StorageUnitsToExponents":{
        "MB": 2,
        "GB": 3,
        "TB": 4,
        "PB": 5,
        "EB": 6,
    }
}

# file size helper for StorageQuota
def format_filesize(number):
    for size in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB']:
       if number < 1024.0 or size == 'PB':
           return "{:.2f} {}".format(number, size)
       number = number / 1024.0

# AccountMessages 
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    account = models.ForeignKey('Account')
    def __str__(self):
        return "[UserProfile] for {}".format(self.user)

class Account(models.Model):
    name = models.CharField(max_length=200, blank=True, default="")
    up_to_date = models.BooleanField(default=False)
    user_quota = models.IntegerField(default=10)
    storage_quota = models.OneToOneField('StorageQuota')
    created_on = models.DateTimeField(null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_on = datetime.now()
        super(Account, self).save(*args, **kwargs)
    def __str__(self):
        return "[Account] {}".format(self.name)

class AccountMessage(models.Model):
    message = models.TextField(blank=True, null=True)
    account = models.ForeignKey("accounts.Account")
    viewed = models.BooleanField(default=False)
    viewed_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    target_url = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return "[Message] for {}".format(self.account)
    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_on = datetime.now()
        if self.viewed and not self.viewed_on:
            self.viewed_on = datetime.now()
        super(AccountMessage, self).save(*args, **kwargs)

class StorageQuota(models.Model):
    amount = models.IntegerField(default=500)
    units = models.CharField(max_length=2, choices=CONSTANTS['StorageUnits'])
    def storage_used(self, human_readable=True):
        unit_conversion = (1024 ** CONSTANTS['StorageUnitsToExponents']['GB'])
        # TODO: 523.51 GB is just stubbed in here as a constant. This should lookup the actual storage consumed for the account.
        used = (523.51 * unit_conversion)
        if human_readable:
            return format_filesize(used)
        return used
    def storage_available(self, human_readable=True):
        unit_conversion = (1024 ** CONSTANTS['StorageUnitsToExponents'][self.units])
        available = (self.amount * unit_conversion) - self.storage_used(human_readable=False)
        if human_readable:
            return format_filesize(available)
        return available
    def __str__(self):
        return "Quota for {}".format(self.account.name)
