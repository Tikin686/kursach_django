from django.views.generic import TemplateView
from blog.views import BlogDetailView
from django.shortcuts import render
from blog.models import Blog
from mailing.models import Mailing, Client
from mailing.services import get_cached_articles


def IndexView(request):
    blogs = Blog.objects.all()

    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(status="started").count()
    unique_clients_count = Client.objects.distinct().count()
    random_articles = get_cached_articles()


    return render(request, 'main/index.html', context={
        'random_articles': blogs,
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients_count': unique_clients_count,
    })
