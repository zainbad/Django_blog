from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('post', 'created_on')
    search_fields = ('name', 'email', 'body')