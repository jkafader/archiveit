from django.db import models

# AccountMessages 
class Account(models.Model):
    

class AccountMessage(models.Model):
    message = models.CharField(max_length=100)
    account = models.ForeignKey("accounts.Account")

class StorageQuota(models.Model):


