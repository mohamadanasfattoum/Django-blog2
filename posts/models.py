from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
from django.utils.text import slugify
'''
    - html widght
    - validation
    - best for db

'''

class Post(models.Model):
    auther = models.ForeignKey(User,related_name='post_auther',on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=1000, null=True)
    content = models.TextField(max_length=50000)
    publish_date = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts',null=True)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self) -> str :
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args, **kwargs)
    


class Comment(models.Model):
    auther = models.ForeignKey(User, related_name='comment_auther', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name= 'comment_Post',on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    creat_date= models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return str(self.post)
    
