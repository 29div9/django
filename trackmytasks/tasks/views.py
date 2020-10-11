from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


def home(request):
    context = {
        'tasks':Task.objects.all()
    }
    return render(request,'tasks/home.html',context)


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/home.html'       #<app_name>/<model>_<view>.html
    context_object_name = 'tasks'
    ordering = ['-reported_on']


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'summary']

    def form_valid(self, form):
        form.instance.assignee = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'summary']

    def form_valid(self, form):
        form.instance.assignee = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.assignee:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.assignee:
            return True
        return False


def about(request):
    return render(request,'tasks/about.html', {'title':'About'})