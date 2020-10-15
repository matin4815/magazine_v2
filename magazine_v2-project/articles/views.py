from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from taggit.models import Tag
from django.http import HttpResponse

def index(request):
  return render(request, 'articles/articles.html')

def article(request, article_slug):

  article = Article.objects.filter(slug = article_slug)
  if article.exists():
    article = article.first()
  else:
    return HttpResponse("<h1>page not found</h1>")
  articles = Article.objects.order_by('-article_date').filter(is_published=True)
 
  context = {
    'article': article,
    'articles': articles
  }

  return render(request, 'articles/article.html', context)

def search(request):
  return render(request, 'articles/articles.html')