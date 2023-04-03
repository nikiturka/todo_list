from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'base/task_create_update.html'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_create_update.html'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
