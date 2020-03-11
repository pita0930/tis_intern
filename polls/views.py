from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import User
from .models import Event
from .forms import EventForm


def index(request):

    return HttpResponse("Hello!")

def event(request):

    events = Event.objects.all()
    context = {
        'events':events
    }
    template = loader.get_template('polls/event.html')
    return HttpResponse(template.render(context, request))

def event_new(request):
    #form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/event/")
    else:
        form = EventForm


    #import pdb; pdb.set_trace()

    return render(request, 'polls/event_new.html', {'form':form,})

def my_page(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    template = loader.get_template('polls/my_page.html')
    return HttpResponse(template.render(context, request))

def talk1(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    template = loader.get_template('polls/talk1.html')
    return HttpResponse(template.render(context, request))
# Create your views here.

