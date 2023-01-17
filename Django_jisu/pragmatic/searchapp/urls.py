
from django.urls import path,include

from searchapp.views import main

app_name = 'searchapp'

urlpatterns = [
    path('', main, name='main'),

]