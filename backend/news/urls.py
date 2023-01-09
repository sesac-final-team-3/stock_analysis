from django.urls import path
from . import views


urlpatterns = [
    # path('graph/',views.news_graph,name='news'),
    path('',views.news_graph,name="news_main"),
]

