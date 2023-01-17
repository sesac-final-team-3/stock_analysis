from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import  ListView
from django.views.generic.edit import FormMixin




class FinancelistView(ListView):
    context_object_name = 'financeapp_list'
    template_name = 'financeapp/list.html'