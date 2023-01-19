from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

import searchapp.views

urlpatterns = [
    path('team3/',searchapp.views.main, name='main'),
    path('team3/articles/', include('articleapp.urls'),name='articleapp'),
    path('team3/news/', include('newsapp.urls'),name='newsapp'),
    path('team3/finanace/', include('financeapp.urls'),name='financeapp'),
    
]