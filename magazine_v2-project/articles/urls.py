from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='articles'),
    path('<slug:article_slug>', views.article ,name='article'),
    path('search', views.search, name='search'),
]
