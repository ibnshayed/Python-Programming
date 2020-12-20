from django.contrib import admin

from .models import Post

# Register your models here.

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display        = ('id', 'title', 'slug', 'author', 'publish', 'status') # makes columns
    list_filter         = ('status', 'created', 'publish', 'author') # enables right side filter options
    search_fields       = ('title', 'body') # search fields on the top
    prepopulated_fields = {'slug': ('title',)} # slug field automatically generated according to title field
    raw_id_fields       = ('author',)
    date_hierarchy      = 'publish'
    ordering            = ('status', 'publish')