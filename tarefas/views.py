from django.shortcuts import render
from tarefas.models import Tasks
import datetime#


def tasks_view(request):
 tasks =  Tasks.objects.all
 print(tasks)
  return render(
 request, 'tasks.html',
{'tarefas':{'tarefa':'ToDo'}}
        
)


