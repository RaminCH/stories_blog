from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(AboutPage)

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
           
    fields = ('title', 'description')
    search_fields = ('title',)
    list_filter = ('create_at',)
    list_display = ('title', 'description')
    #readonly_fields = ('title',) #we can't edit anymore title
    ordering = ('-create_at',)

@admin.register(NavLinks)
class NavLinksAdmin(admin.ModelAdmin):
    fields = ('title', 'url', 'active',)
    list_filter = ('active',)
    list_display = ('title', 'url', 'active',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'subject', 'message',)
    list_filter = ('created_at',)
    list_display = ('name', 'email', 'subject','created_at')

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'description', 'category', 'owner')
    list_display = ('title', 'category', 'owner')
    list_filter = ('created_at',)
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'image',)
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'description', 'category', 'long_description', 'owner' )
    list_display = ('title', 'category',)
    list_filter = ('created_at',)
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'story')
