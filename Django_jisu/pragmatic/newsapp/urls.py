from django.urls import path

from newsapp.views import NewsListView

app_name = 'news'

urlpatterns = [
    path('list/', NewsListView.as_view(), name='list'),

]