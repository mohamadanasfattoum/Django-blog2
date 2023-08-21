from django.contrib import admin

# Register your models here.

from .models import post, Comment



admin.site.register(post)
admin.site.register(Comment)