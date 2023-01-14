from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView

from articleapp.models import Article
from newsapp.models import News

class NewsListView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'newsapp/list.html'
    paginate_by = 3
    

    def get_queryset(self):
        return News.objects.all().order_by('pk')