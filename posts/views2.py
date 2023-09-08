from django.views import generic
from .models import post

'''
template: post_list.html
context: post_list , object_list
'''

class PostList(generic.ListView):
    model = post   # Query: database



'''
template: post_detail.html
context: post , object
'''

class PostDetail(generic.DetailView):
    model = post



class PostCreate(generic.CreateView):
    model = post
    fields='__all__'
    success_url= '/blog/'



class PostUpdate(generic.UpdateView):
    model= post
    fields='__all__'
    success_url= '/blog/'
    template_name='posts/edit.html'
