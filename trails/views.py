from django.views import generic
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class HikeList(TemplateView):
    template_name = 'about.html'

class HikeDetail(TemplateView):
    template_name = 'search.html'