from django.views import generic
from .models import post

'''
template: post_list.html
context: post_list , object_list
'''

class PostList(generic.ListView):
    modol = post   # Query: database
