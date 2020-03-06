from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from .models import Event

def index(request):

    events = Event.objects.all()
    context = {
        'events':events
    }
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context, request))

def makeEvent(request):
    return HttpResponse(template)


# Create your views here.
