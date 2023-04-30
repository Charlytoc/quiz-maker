from .views import answer_from_a_template, retrieve_templates
from django.urls import path
# ALL THIS FILE WAS ADDED BY ME
app_name = 'ai-module'
urlpatterns = [
    path('answer', answer_from_a_template, name='hello'),
    path('templates/list', retrieve_templates, name='templates list'),

]