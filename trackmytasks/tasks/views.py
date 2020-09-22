from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def home(request):
    context = {
        'tasks':Task.objects.all()
    }
    return render(request,'tasks/home.html',context)


def about(request):
    return render(request,'tasks/about.html', {'title':'About'})