from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Comment

class PostAdmin(SummernoteModelAdmin):
    list_display = ['title' , 'publish_date']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)