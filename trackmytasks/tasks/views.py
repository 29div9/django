from django.shortcuts import render
from django.http import HttpResponse


tasks = [
    {
        'title':'First task',
        'assignee':'Divya Kumari',
        'reported_on':'September 21, 2020',
        'summary':'First task on portal'
    },
    {
        'title': 'Second task',
        'assignee': 'Jane Doe',
        'reported_on': 'September 26, 2020',
        'summary': 'Second task on portal'
    },
]


def home(request):
    context = {
        'tasks':tasks
    }
    return render(request,'tasks/home.html',context)


def about(request):
    return render(request,'tasks/about.html', {'title':'About'})