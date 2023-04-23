from django.db import models
from django.contrib.auth.models import User
# Create your models here.
DRAFT = 'DRAFT'
ANSWERING = 'ANSWERING'
DONE = 'DONE'
TRIVIA_STATUS = (
    (DRAFT, 'DRAFT'),
    (ANSWERING, 'ANSWERING'),
    (DONE, 'DONE'),
)


class Post(models.Model):
    title = models.CharField(max_length=100, default=None)
    url = models.CharField(max_length=200, default=None, null=True, blank=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=True)
    status = models.CharField(max_length=9, choices=TRIVIA_STATUS, default=DRAFT)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
