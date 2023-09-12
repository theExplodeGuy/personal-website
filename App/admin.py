from django.contrib import admin

# Register your models here.
from .models import Post, Home, Comment, Project


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'created_on')

class QualAdmin(admin.ModelAdmin):
    list_display = ('qualification', 'created_on')
    search_fields = ['about_qualification', 'qualification']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'technology')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Home, QualAdmin)
admin.site.register(Project, ProjectAdmin)