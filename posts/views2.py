from django.views import generic
from .models import post

class PostList(generic.ListViews):
    modol = post   # Query: database
    