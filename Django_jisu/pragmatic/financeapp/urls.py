from django.urls import path
from django.views.generic import TemplateView

from financeapp.views import FinancelistView

app_name = 'finance'

urlpatterns = [
    path('<int:searched_code>/', FinancelistView.as_view(), name='finance')
]