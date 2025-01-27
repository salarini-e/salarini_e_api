from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
class Post(models.Model):
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    descricao = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='blog/imagem/', blank=True, null=True) 
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    dt_inclusao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    def get_imagem(self):
        if self.imagem:
            return self.imagem.url
        return '/static/images/sem_foto.png'