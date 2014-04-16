from django.contrib import admin
from wireframe.archiveit.models import Collection, CollectionTopic, Seed, SeedCapturePattern, SeedFolder, SeedScopeRule, Crawl, Comment

# Register your models here.
class CollectionAdmin(admin.ModelAdmin):
    list_display =('name',)
admin.site.register(Collection, CollectionAdmin)

class CollectionTopicAdmin(admin.ModelAdmin):
    list_display =('name',)
admin.site.register(CollectionTopic, CollectionTopicAdmin)

class SeedAdmin(admin.ModelAdmin):
    list_display =('url',)
admin.site.register(Seed, SeedAdmin)

class SeedCapturePatternAdmin(admin.ModelAdmin):
    list_display =('name',)
admin.site.register(SeedCapturePattern, SeedCapturePatternAdmin)

class SeedFolderAdmin(admin.ModelAdmin):
    list_display =('name',)
admin.site.register(SeedFolder, SeedFolderAdmin)

class SeedScopeRuleAdmin(admin.ModelAdmin):
    list_display =('__str__',)
admin.site.register(SeedScopeRule, SeedScopeRuleAdmin)

class CrawlAdmin(admin.ModelAdmin):
    list_display =('__str__',)
admin.site.register(Crawl, CrawlAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display =('__str__',)
admin.site.register(Comment, CommentAdmin)

