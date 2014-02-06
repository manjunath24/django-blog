from django.shortcuts import render

from agiliq_app.models import Article

# Create your views here.


def home(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'articles': articles, 'home': True})


def about(request):
    return render(request, 'about.html', {'about': True})
