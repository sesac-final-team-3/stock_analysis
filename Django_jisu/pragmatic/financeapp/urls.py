from django.urls import path
from . import views


app_name = 'financeapp'

urlpatterns = [
    path('<int:searched_code>/',views.finance_data,name='finance_data'),
    
]
