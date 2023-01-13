from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name = 'articleapp'

urlpatterns = [
    path('list/373220/', ArticleListView.as_view(), name='list')
]