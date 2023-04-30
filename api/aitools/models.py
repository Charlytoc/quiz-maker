from django.db import models
from django.utils.text import slugify
import re
from django.contrib.auth.models import User



class TemplateAI(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(blank=True, null=True, default=None)
    prompt = models.TextField(max_length=3499,help_text='This will be the body of the prompt, what the AI will receive to provide an answer', null=True)
    human_example= models.CharField(max_length=500, null=True, blank=True)
    ai_example= models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        from .actions import track_template_versions
        self.find_variables()
        self.slug = slugify(self.name)
        self.variables = self.find_variables()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        track_template_versions(self)



    

class TemplateAIVersion(models.Model):

    number = models.IntegerField(default=1)
    template = models.ForeignKey(TemplateAI, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

PENDING = 'PENDING'
ERROR = 'ERROR'
SUCCESS = 'SUCCESS'
STATUS = (
    (PENDING, 'Pending'),
    (ERROR, 'Error'),
    (SUCCESS, 'Success'),
)

class CompletionJob(models.Model):
    template = models.ForeignKey(TemplateAI, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    status = models.CharField(max_length=9, choices=STATUS, default=PENDING)
    status_text = models.TextField(default=None, null=True, blank=True)

    inputs = models.JSONField(help_text="User value for template variables", null=True, blank=True)
    prompt = models.TextField(default=None, null=True, blank=True)
    answer = models.TextField(default=None, null=True, blank=True)

    started_at = models.DateTimeField( editable=True, blank=True, null=True)
    ended_at = models.DateTimeField(editable=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)