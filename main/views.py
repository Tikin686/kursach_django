from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/base.html'
    extra_context = {
        'title': 'Главная страница',
    }