from django.shortcuts import render

# Create your views here.
from .models import Question
from django.shortcuts import render
from django.http import HttpResponse, response


def index(request):
    # return HttpResponse("Hello, World")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
def detail(request, question_id):
    return HttpResponse("You are looking at question %s"%question_id)
def results(request, question_id):
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("You are voting on question %s"%question_id)