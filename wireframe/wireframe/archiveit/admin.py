from django.contrib import admin
from wireframe.archiveit.models import Collection, CollectionTopic, Seed, SeedCapturePattern, SeedGroup, SeedFolder, SeedScopeRule, Crawl, Comment

# Register your models here.
class CollectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Collection, CollectionAdmin)

class CollectionTopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(CollectionTopic, CollectionTopicAdmin)

class SeedAdmin(admin.ModelAdmin):
    pass
admin.site.register(Seed, SeedAdmin)

class SeedCapturePatternAdmin(admin.ModelAdmin):
    pass
admin.site.register(SeedCapturePattern, SeedCapturePatternAdmin)

class SeedGroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(SeedGroup, SeedGroupAdmin)

class SeedFolderAdmin(admin.ModelAdmin):
    pass
admin.site.register(SeedFolder, SeedFolderAdmin)

class SeedScopeRuleAdmin(admin.ModelAdmin):
    pass
admin.site.register(SeedScopeRule, SeedScopeRuleAdmin)

class CrawlAdmin(admin.ModelAdmin):
    pass
admin.site.register(Crawl, CrawlAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)

