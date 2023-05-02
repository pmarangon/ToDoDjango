from django.contrib import admin
from tarefas.models import Tasks


class TasksAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'disciplina', 'deadline')
    search_fields = ('deadline',)


admin.site.register(Tasks, TasksAdmin)
