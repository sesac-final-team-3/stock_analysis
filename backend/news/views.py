from django.shortcuts import render,HttpResponse
def news_graph(request):
    return render(request,'newsgraph.html')

# def news_page(request):
    # return render(request,'list.html')