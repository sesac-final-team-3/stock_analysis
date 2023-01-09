from django.shortcuts import render,HttpResponse
def summary(request):
    return render(request,'summary.html')