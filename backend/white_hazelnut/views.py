from django.shortcuts import render
from django.http import HttpResponseNotFound
from summary.models import TbName

# def homepage(request):
#     if request.method == "POST":
#         return render(request,'index.html',context={'text':'POST METhod'})
#     else:
#         return render(request,'index.html',context={'text':'GET MEthod!'})
# def homepage(request):
#     print('접속?')
#     if request.method == "POST":
#         # print('@@@@',help(request.POST.get()))
#         print('---'*20,'\n',request.POST)
#         searching=request.POST.get("stock_search",default='test') # 검색어
#         # searching=request.GET["stock_search"] # 검색어
#         print('@123123',searching)
#         # # main table 
#         company_info=TbName.objects.filter(name=searching)
#         # 검색어 -> code
#         searched_code = int(company_info.values()[0]['code'])
#         print('!!!!',searched_code) # 372220
#         return render(request, 'index.html',context={'text':searching})
#         print('!!!!',request.method)
#         return render(request,'index.html')
#     else:
#         print('@esle?')
#         return render(request,'index.html')

def homepage(request):
    print('간단하게진입')
    return render(request,'index.html')


# def error_404_view(request,exception):
#     return HttpResponseNotFound("The page is not found!")
