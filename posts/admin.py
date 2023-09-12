from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title' , 'publish_date']

admin.site.register(Post)
admin.site.register(Comment)