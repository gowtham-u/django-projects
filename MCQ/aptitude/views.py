from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from aptitude.models import Question, Answer, Subject

def index(request):
    return HttpResponse("hello world")
    
def get_question_info(request, subject_id):
    subject = Subject.objects.get(id = subject_id)
    question = Question.objects.get(subject = subject)
    answers = Answer.objects.filter(question = question)
    print(answers)
    answers_info = []

    for lst_info in answers:
        answers_info_id = {'related_text':lst_info.related_text,'id':lst_info.id}
        answers_info.append(answers_info_id)


    question_name = {
        'question':{
            'id': question.id,
            'serial_no':question.serial_no,
            'heading':question.heading,
            'definition':question.definition,
            'subject': question.subject},
            'answer':answers_info
            
    }

    return JsonResponse(question_name)
