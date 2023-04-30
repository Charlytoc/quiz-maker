from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .actions import execute_a_template
from .models import TemplateAI
from .serializers import TemplateAISerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
# Create your views here.

@csrf_exempt
def answer_from_a_template(request):
    """
    This view is to provide an answer based in a template, it will receive two inputs:
    REQUEST BODY
    {
        template_id= int,
        user_input = str
    }
    And will return an answer in str format like:
    RESPONSE BODY
    {
        ai_answer: str,
        status: int,
    }
    """

    if request.method == 'POST':
        request_data = json.loads(request.body)
        template_id = request_data.get('template_id')
        user_input = request_data.get('user_input')

        template = TemplateAI.objects.filter(id=template_id).first()


        status = 200
        ai_answer = execute_a_template(template, user_input)
        response_data = {
            'ai_answer': ai_answer,
            'status': status,
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['GET'])
def retrieve_templates(request):
    """
    Retrieve all TemplateAI objects using TemplateAISerializer
    """
    templates = TemplateAI.objects.all()
    serializer = TemplateAISerializer(templates, many=True)
    return JsonResponse(serializer.data, safe=False)

