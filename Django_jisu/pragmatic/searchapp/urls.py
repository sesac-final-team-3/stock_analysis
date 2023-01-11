
from django.urls import path

from searchapp.views import main,testpage

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),

]