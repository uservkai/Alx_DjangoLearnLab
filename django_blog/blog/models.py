from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model): # blog post model
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager() #replaces the ManyToManyField for tags
    # tags = models.ManyToManyField('Tag', blank=True)
    
    def __str__(self):
        return f"{self.title} by {self.author.username}"
    

class Profile(models.Model): #model for user profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
class Comment(models.Model): # model for comments on blog posts
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    
class Tag(models.Model): #model for tags associated with posts
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name