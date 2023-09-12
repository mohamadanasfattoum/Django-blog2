from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Comment



admin.site.register(Post)
admin.site.register(Comment)