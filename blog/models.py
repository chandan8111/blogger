from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    

    def __str__(self):
        return self.title + " by " + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    time = models.DateTimeField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment[0:40] + " ... " + "by " + self.user.username