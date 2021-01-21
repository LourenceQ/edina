from django.db import models

# Create your models here.

class usuario(models.Model):
#    cell = models.IntField(max_length = 20)
    email = models.EmailField(max_length=254, unique=True)
#   agendamento = TextField()
