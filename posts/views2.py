from django.views import generic
from .models import Post

'''
template: post_list.html
context: post_list , object_list
'''

class PostList(generic.ListView):
    model = Post   # Query: database



'''
template: post_detail.html
context: post , object
'''

class PostDetail(generic.DetailView):
    model = Post



class PostCreate(generic.CreateView):
    model = Post
    fields='__all__'
    success_url= '/blog/'



class PostUpdate(generic.UpdateView):
    model= Post
    fields='__all__'
    success_url= '/blog/'
    template_name='posts/edit.html'



class PostDelete(generic.DeleteView):
    model= Post
    success_url= '/blog/'