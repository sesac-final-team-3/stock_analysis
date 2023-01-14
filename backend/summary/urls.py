from django.urls import path
from . import views


urlpatterns = [
    path('',views.summary,name='summary'),
    path('<int:searched_code>/',views.summary,name='summary'),
]

