from django.db import models

class Cliente(models.Model):
    email_cliente = models.CharField(max_length=100)
    senha_cliente = models.CharField(max_length=100)

class Imagens(models.Model):
    camisa_venda = models.ImageField
    
