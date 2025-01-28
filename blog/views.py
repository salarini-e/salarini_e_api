from typing import Any, Dict
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post

def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({
                         'message': 'API for blog',
                         'to get all posts': '/get-articles/',
                         'to get a specific post': '/get-article/<slug>/'
                         }, status=200)

def posts(request: HttpRequest) -> JsonResponse:
    posts = Post.objects.all().order_by('-id')[:15]
    data: Dict[str, Any] = {'status': 200, 'articles': []}

    for post in posts:
        data['articles'].append({
            'id': post.id,
            'slug': post.slug,
            'titulo': post.titulo,
            'conteudo': post.conteudo,
            'descricao': post.descricao,
            'autor': post.autor.nome,
            'categorias': [c.nome for c in post.categorias.all()],
            'dt_inclusao': post.dt_inclusao.strftime('%d/%m/%Y %H:%M'),
            'imagem': post.get_imagem()
        })

    return JsonResponse(data, status=200)

def get_post(request: HttpRequest, slug: str) -> JsonResponse:
    post = get_object_or_404(Post, slug=slug)
    data: Dict[str, Any] = {
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
