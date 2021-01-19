from django.db import models

# Create your models here.

class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return 'Message from' + self.name
    