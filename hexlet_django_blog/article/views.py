from django.shortcuts import render
from django.views.generic import ListView
from hexlet_django_blog.article import models


class ArticleListView(ListView):
    model = models.Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
