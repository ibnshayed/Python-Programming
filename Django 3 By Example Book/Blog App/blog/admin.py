from django.contrib import admin

from .models import Post, Comment

# Register your models here.

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # list_display        = ('id', 'title', 'slug', 'author', 'publish', 'status') # makes columns
    list_display        = [field.name for field in Post._meta.fields] # makes all columns
    list_filter         = ('status', 'created', 'publish', 'author') # enables right side filter options
    search_fields       = ('title', 'body') # search fields on the top
    prepopulated_fields = {'slug': ('title',)} # slug field automatically generated according to title field
    raw_id_fields       = ('author',) # author field now get just author id not full object
    date_hierarchy      = 'publish'
    ordering            = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    # list_display        = ('name', 'email', 'post', 'created', 'active')
    list_display        = [field.name for field in Comment._meta.fields] # makes all columns
    list_filter         = ('active', 'created', 'updated')
    search_fields       = ('name', 'email', 'body')













