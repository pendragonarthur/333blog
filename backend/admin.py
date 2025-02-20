from django.contrib import admin
from .posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'posted_at')
    search_fields = ('title', 'content', 'author')
    list_filter = ('posted_at',)