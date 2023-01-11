from django.shortcuts import render,HttpResponse
from .models import TbName
def summary(request):
    print(request.POST['stock_search'])
    searching=request.POST.get("stock_search")
    print('summary의',searching)
    print('####',TbName.objects.filter(name=searching))
    result=TbName.objects.filter(name=searching)
    # code_result=TbName.objects.filter()
    return render(request,'test.html',{'code':result})
    # return render(request,'test.html')

# def getTbNameAll(request):
#     if request.method == "POST":
#         print(request.POST.stock_search)
        
#         return render(request,'index.html',context={'text':'POST METhod'})
#     else:
#         print('****'*10)
#         data = TbName.objects.all()[0:5] #1 # 받아올 페이지 
#         print('!!!!',data)
#         return render(request, 'test.html',{'summary':data})
#         # return render(request,'index.html',context={'text':'GET MEthod!'})


    # 리다이렉트시키고 쿼리준것을 같이줘야한다. 