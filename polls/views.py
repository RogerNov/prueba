from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render
# Create your views here.

def index(request):
    lastes_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question for q in latest_question_list])
    #return HttpResponse(output)
   #esto es con el  template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':lastes_question_list
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html',context)



   #estos son datos que se mostrar en la vista y seran llamada atraves del patron url 
def detail(request, question_id):
    #response = "Estas mirando las preguntas %s."
    
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("La pregunta no existe!")   
    return render(request, 'polls/detail.html', {'question':question})



    
def results(request, question_id):
    response = "Estas viendo los resultado de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s." % question_id)