from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.homepage),
    path("news/",include('news.urls'),name='news'),
    path("summary/",include('summary.urls'),name='summary'),
]

# handler404='white_hazelnut.views.error_404_view'