from django.contrib import admin
from .models import CredentialsOpenAI
# Register your models here.

@admin.register(CredentialsOpenAI)
class CredentialsOpenAIAdmin(admin.ModelAdmin):
    list_display = ('id', 'token', 'user')
