from django.shortcuts import render
from django.http import HttpResponseNotFound
# def homepage(request):
#     if request.method == "POST":
#         return render(request,'index.html',context={'text':'POST METhod'})
#     else:
#         return render(request,'index.html',context={'text':'GET MEthod!'})
# def homepage(request):
    # if request.method == "POST":
    #     searching=request.POST.get("stock_search") # 검색어

    #     return render(request, 'index.html',context={'text':searching})
    # else:
    #     return render(request,'index.html')

def homepage(request):
    return render(request,'index.html')

# def error_404_view(request,exception):
#     return HttpResponseNotFound("The page is not found!")
