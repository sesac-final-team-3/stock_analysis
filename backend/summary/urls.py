from django.urls import path
from . import views


urlpatterns = [
    path('',views.summary,name='summary'),
    # path('1',views.getTbNameAll,name='TbName'),
]

