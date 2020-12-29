from django.contrib import admin
from .models import *

admin.site.register(Calculate)
admin.site.register(Tags)

# Project
class ProjectsImageAdmin(admin.StackedInline):
    model = Images
 
@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectsImageAdmin]
 
    class Meta:
       model = Projects
 
@admin.register(Images)
class ProjectsImageAdmin(admin.ModelAdmin):
    pass

# News
class NewImageAdmin(admin.StackedInline):
    model = Images_news
 
@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    inlines = [NewImageAdmin]
 
    class Meta:
       model = News
 
@admin.register(Images_news)
class NewImageAdmin(admin.ModelAdmin):
    pass