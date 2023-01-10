from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name = 'articleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),

    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]