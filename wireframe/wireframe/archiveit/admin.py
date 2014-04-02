from django.contrib import admin
from wireframe.archiveit.models import Collection, Seed, SeedGroup, SeedFolder, SeedScopeRule, Crawl, Comment

# Register your models here.
class CollectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Collection, CollectionAdmin)

class SeedAdmin(admin.ModelAdmin):
    pass
admin.site.register(Seed, SeedAdmin)

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

