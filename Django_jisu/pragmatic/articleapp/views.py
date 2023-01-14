from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import  ListView
from django.views.generic.edit import FormMixin

from articleapp.models import Article



class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'

    def get_queryset(self):
        return Article.objects.all().order_by('-pk')