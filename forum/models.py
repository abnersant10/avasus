from django.db import models
from .manager import *
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = None
    nome_completo = models.CharField(max_length=60)
    cpf = models.CharField(unique=True, max_length=11)
    objects = UserManager()
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []
