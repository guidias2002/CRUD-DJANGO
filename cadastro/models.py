from django.db import models

class Pessoa(models.Model):

    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=14)
    email = models.EmailField(max_length=30)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome




   
