from django.shortcuts import render,HttpResponse
from .models import TbName,TbSentimental,TbReport
from finance.models import TbOHLCV

import json

def summary(request):
    """
    Summary page 에 필요한 정보를 가지고 온다.
    """
    print('###',request.POST['stock_search'],'이 검색 되었습니다.')
    searching=request.POST.get("stock_search")

    # main table 
    company_info=TbName.objects.filter(name=searching)
    # 검색어 -> code
    searched_code = int(company_info.values()[0]['code'])
    # print('@@@',searched_code)

    # comment value
    senti_info = TbSentimental.objects.filter(code=searched_code)
    # 마지막 값 가지고 오고 싶은데, negative indexing 이 안됨
    temp=len(senti_info.values())
    comment_info=senti_info.values()[temp-2]['comment']

    # comment value string 인 것들 dict 화
    comment_value=json.loads(comment_info.replace("'", "\""))
    print(comment_value)


    # analyst opinion
    report_info = TbReport.objects.filter(code=searched_code)
    a_opinion=report_info.values()[0]['comment']
    
    # OHLCV data 진행예정
    ohlcv_info = TbOHLCV.objects.filter(code=searched_code)
    ohlcv = ohlcv_info.values()
    
    return render(request,'test.html',{'code':company_info,'comment_value':comment_value,'a_opinion':a_opinion})
