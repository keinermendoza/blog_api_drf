from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']
    search_fields = ['title', 'author', 'body']
    date_hierarchy = 'created'
