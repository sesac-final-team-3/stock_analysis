from django.urls import path

from newsapp.views import NewsListView, NewsCreateView, NewsDetailView, NewsUpdateView, NewsDeleteView

app_name = 'news'

urlpatterns = [
    path('list/', NewsListView.as_view(), name='list'),

    path('create/', NewsCreateView.as_view(), name='create'),
    path('detail/<int:pk>', NewsDetailView.as_view(), name='detail'),
    path('update/', NewsUpdateView.as_view(), name='update'),
    path('delete/', NewsDeleteView.as_view(), name='delete'),
]