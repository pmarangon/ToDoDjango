from django.contrib import admin
from tarefas.models import Tasks, Disciplina


class TasksAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'disciplina', 'deadline')
    search_fields = ('deadline',)


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(Tasks, TasksAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
