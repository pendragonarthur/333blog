from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_by', 'created_at')
    search_fields = ('title', 'content', 'created_by')
    list_filter = ('created_at',)