from django.db import models


class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    tarefa = models.CharField(max_length=50)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name='tasks_disciplina')
    deadline = models.DateField()

    def __str__(self):
        return self.tarefa
