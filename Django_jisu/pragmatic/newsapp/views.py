from django.shortcuts import render,HttpResponse
def news_graph(request,searched_code):
    data={'code':searched_code}
    return render(request,'newsapp/list.html',data)