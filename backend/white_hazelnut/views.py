from django.shortcuts import render,HttpResponse
# def homepage(request):
#     if request.method == "POST":
#         return render(request,'index.html',context={'text':'POST METhod'})
#     else:
#         return render(request,'index.html',context={'text':'GET MEthod!'})
def homepage(request):
    if request.method == "POST":
        searching=request.POST.get("stock_search")

        return render(request, 'index.html',context={'text':searching})
    else:
        return render(request,'index.html')