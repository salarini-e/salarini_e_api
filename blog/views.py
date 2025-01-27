from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def index(request):
    return JsonResponse({'message':'Hello, World!'})

def posts(request):
    # return JsonResponse({'status': 200, 'message':'Hello, World!'})
    posts = Post.objects.all().order_by('-id')[:15]
    data = {'status': 200, 'articles': []}
    for post in posts:
        data['articles'].append({
            'id': post.id,
            'titulo': post.titulo,
            'conteudo': post.conteudo,
            'descricao': post.descricao,
            'autor': post.autor.nome,
            'categorias': [c.nome for c in post.categorias.all()],
            'dt_inclusao': post.dt_inclusao.strftime('%d/%m/%Y %H:%M'),
            'imagem': post.get_imagem()
        })  
        data
    return JsonResponse(data, status=200)

def get_post(request, id):
    post = Post.objects.get(id=id)
    data = {
        'status': 200,
        'article': {
            'titulo': post.titulo,
            'conteudo': post.conteudo,
            'descricao': post.descricao,
            'autor': post.autor.nome,
            'categorias': [c.nome for c in post.categorias.all()],
            'dt_inclusao': post.dt_inclusao.strftime('%d/%m/%Y %H:%M'),
            'imagem': post.get_imagem()
        }
    }
    return JsonResponse(data, status=200)
