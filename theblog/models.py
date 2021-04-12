from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        #return reverse("article-detail", args=(str(self.id)))
        return reverse("home")

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.user)
        
class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default='test')
    # likes = models.ManyToManyField(User, related_name='blog_posts')
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse("article-detail", args=(str(self.id)))
        return reverse("home")

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.post.title} - {self.name}"
    