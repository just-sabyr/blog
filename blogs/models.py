from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """a Post. """
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # for uploading files:
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/',max_length=250,null=True, default=None)

    def __str__(self):
        return self.title

class Comment(models.Model):
    "Comment for each Post."
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"