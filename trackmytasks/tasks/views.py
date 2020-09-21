from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to trackmytasks!</h1>")


def about(request):
    return HttpResponse("<h1>About page</h1>")