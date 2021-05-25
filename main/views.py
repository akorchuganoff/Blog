from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'last_article_id': 3
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    return render(request, 'main/about.html')

def life(request):
    return render(request, 'main/life.html')

def offer(request):
    return render(request, 'main/job_offer.html')