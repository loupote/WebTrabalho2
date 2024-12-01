from django.db import models

from django.utils import timezone


# Create your models here.

class Participante1(models.Model):
    user_id = models.AutoField(primary_key=True)
    nome = models.TextField(db_column='NOME')
    sobrenome = models.TextField(db_column='SOBRENOME')
    genero = models.TextField(db_column='GENERO')
    dtNasc = models.DateField(db_column='DTNASC')
    idade = models.PositiveIntegerField(db_column='IDADE')
    distancia = models.TextField(db_column='DISTANCIA')
    email = models.EmailField(max_length=254)

    class Meta:
        managed = True
        db_table = 'corrida_pessoa'
        ordering = ['user_id']

    def __str__(self):
        return self.nome
    
    def get_idade(self):
        today = timezone.now().date()
        idade = today.year - self.dtNasc.year

        if (today.month, today.day) < (self.dtNasc.month, self.dtNasc.day):
            idade -= 1

        return idade
    
    def save(self, *args, **kwargs):
        self.idade = self.get_idade()
        super().save(*args, **kwargs)


DISTANCE_CHOICES = [
        (5, '5 quilômetros'),
        (10, '10 quilômetros'),
        (21, '21 quilômetros'),
    ]


class Participante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(db_column='NOME')
    sobrenome = models.TextField(db_column='SOBRENOME')
    distancia = models.IntegerField(db_column='DISTANCIA', choices=DISTANCE_CHOICES)
    tempo = models.TextField(db_column='TEMPO', max_length=20)

    class Meta:
        managed = True
        db_table = 'RunnersList'
        ordering = ['sobrenome']

    def __str__(self):
        return self.nome