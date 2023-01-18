from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

import searchapp.views

urlpatterns = [
    path('',searchapp.views.main, name='main'),
    path('articles/', include('articleapp.urls'),name='articleapp'),
    path('news/', include('newsapp.urls'),name='newsapp'),
    path('finanace/', include('finanaceapp.urls'),name='financeapp'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)