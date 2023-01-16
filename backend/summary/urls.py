from django.urls import path
from . import views

app_name="summary"

urlpatterns = [
    path('<int:searched_code>/',views.summary_result,name='summary_result'),
    path('search/',views.searching_db,name='searching_db'),
]

