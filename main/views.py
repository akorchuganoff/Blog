from django.shortcuts import render, HttpResponse

def index(request):
    data = {
        'last_article_id': 1
    }
    return render(request, 'main/index.html', data=data)

def about(request):
    return render(request, 'main/about.html')

def life(request):
    return render(request, 'main/life.html')

def offer(request):
    return render(request, 'main/job_offer.html')