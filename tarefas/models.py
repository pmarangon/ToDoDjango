from django.db import models


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    tarefa = models.CharField(max_length=20)
    disciplina = models.CharField(max_length=20)
    deadline = models.DateField()