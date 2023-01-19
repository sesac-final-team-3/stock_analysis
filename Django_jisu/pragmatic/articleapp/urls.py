from django.urls import path
from django.views.generic import TemplateView


from . import views

app_name = 'articleapp'

urlpatterns = [
    path('<int:searched_code>/',views.summary_result,name='summary_result'),
    path('search/',views.searching_db,name='searching_db')
]