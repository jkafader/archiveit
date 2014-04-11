from django.contrib import admin
from wireframe.accounts.models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileAdmin)

class AccountAdmin(admin.ModelAdmin):
    pass
admin.site.register(Account, AccountAdmin)

class AccountMessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(AccountMessage, AccountMessageAdmin)

class StorageQuotaAdmin(admin.ModelAdmin):
    pass
admin.site.register(StorageQuota, StorageQuotaAdmin)
