from django.urls import path
from django.views.generic import TemplateView

from financeapp.views import FinancelistView

app_name = 'finance'

urlpatterns = [
    path('', FinancelistView.as_view(), name='finance')
]