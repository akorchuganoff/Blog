from django.shortcuts import render
from articles.models import Article

def index(request):
    articles = Article.objects.order_by('-date_of_pub').all()

    for a in articles:
        print(a.date_of_pub)

    articles_blocks_of_3 = []
    count = 0
    now = []
    for a in articles[1:]:
        if count != 3:
            count += 1
            now.append(a)
        else:
            count = 0
            articles_blocks_of_3.append(now)
            now = []

    articles_blocks_of_3.append(now)

    context = {
        'last_article': articles[0],
        'articles': articles[1:],

    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html')
