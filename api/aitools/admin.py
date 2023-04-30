from django.contrib import admin
from .models import TemplateAI, TemplateAIVersion
# Register your models here.
from django.contrib import admin


@admin.register(TemplateAI)
class TemplateAIAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(TemplateAIVersion)
class TemplateAIVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'template', 'body')
