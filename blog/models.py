from typing import Optional
from django.db import models
from django.db.models import (
    ForeignKey as fk,
    ManyToManyField as manytomany,
    ImageField as img,
    DateTimeField as datetime,
)
from django.utils.text import slugify

class Autor(models.Model):
    nome: str = models.CharField(max_length=100)
    data_criacao: datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.nome


class Categoria(models.Model):
    nome: str = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nome


class Post(models.Model):
    slug: str = models.SlugField(max_length=150, unique=True, null=True, blank=True)
    titulo: str = models.CharField(max_length=150)
    conteudo: str = models.TextField()
    descricao: Optional[str] = models.TextField(null=True, blank=True)
    imagem: Optional[img] = models.ImageField(
        upload_to='blog/imagem/', blank=True, null=True
    )
    autor: fk = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categorias: manytomany = models.ManyToManyField(Categoria)
    dt_inclusao: datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.titulo
    
    def get_imagem(self) -> str:
        if self.imagem:
            return self.imagem.url
        return '/static/images/sem_foto.png'

    def save(self, *args, **kwargs) -> None:
            if not self.slug:
                self.slug = slugify(self.titulo)
            super().save(*args, **kwargs)