from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

import searchapp.views

urlpatterns = [
    path('',searchapp.views.main, name='main'),
    path('articles/', include('articleapp.urls'),name='articleapp'),
    path('news/', include('newsapp.urls'),name='newsapp'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)