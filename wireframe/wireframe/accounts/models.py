from django.db import models

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
    def __unicode__(self):
        "[UserProfile] for {}".format(self.user)

class Account(models.Model):
    up_to_date = models.BooleanField(default=False)
    user_quota = models.IntegerField(default=10)
    storage_quota = models.OneToOneField('StorageQuota')

class AccountMessage(models.Model):
    message = models.CharField(max_length=100)
    account = models.ForeignKey("accounts.Account")

class StorageQuota(models.Model):
    amount = models.IntegerField(default=500)
    units = models.CharField(max_length=2, choices=CONSTANTS['StorageUnits'])
    def storage_used(self, human_readable=True):
        unit_conversion = (1024 ** CONSTANTS['StorageUnitsToExponents']['GB'])
        # TODO: 523 is just stubbed in here as a constant. This should lookup the actual storage consumed for the account.
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
