from django.urls import path
from . import views


app_name = 'newsapp'

urlpatterns = [
    path('<int:searched_code>/',views.news_graph,name='news_graph'),
    # path('search/',views.news_graph,name="news_main"),
]
