from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def main(request):
    return  render(request,'searchapp/main.html')

def search_page(request):
    return  render(request,'articles/list.html')