from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('get-articles/', views.posts, name='posts'),
    path('get-article/<slug>/', views.get_post, name='get_post'),
]   