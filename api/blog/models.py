from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, default=None)
    image = models.CharField(max_length=200, default=None, null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

class Threat(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    threat = models.ForeignKey(Threat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=True)

class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sended_message')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_message')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    