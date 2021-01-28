from django.db import models

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