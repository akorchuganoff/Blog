from django.shortcuts import render
from django.http import HttpResponse


def article(article_id):
    data = {
        'article_id': article_id
    }
    return render('articles/article.html', data=data)