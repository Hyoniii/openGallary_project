from django.shortcuts import render
from polls.models     import Question

def index(request):
    latest_question_list = Question.objects.all().order_by('id')[:5]
