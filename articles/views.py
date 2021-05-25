from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def article(request, article_id):

    main_article = Article.objects.filter(id=article_id).first()
    context = {
        'article': main_article
    }
    print(main_article.Title, main_article.Header_on_article_page)
    return render(request, 'articles/article.html', context=context)