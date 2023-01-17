from django.shortcuts import render,HttpResponse
def news_graph(request):
    return render(request,'newsapp/list.html')