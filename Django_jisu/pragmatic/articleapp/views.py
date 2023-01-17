from django.shortcuts import render

# Create your views here.
# from django.urls import reverse, reverse_lazy

from articleapp.models import TbName, TbReport, TbSentimental
from finanaceapp.models import TbOHLCV
import json
from django.shortcuts import redirect


def searching_db(request):
    """
    searching에서 받은 code 조회
    """
    print('###convert 접속')
    searching=request.POST.get('stock_search')
    print('@@@@',searching)
    company_info=TbName.objects.filter(name=searching)
    searched_code = str(company_info.values()[0]['code']) #.first()
    print(f'{searched_code}를 검색합니다.')

    return redirect('articleapp:summary_result',searched_code)

def summary_result(request,searched_code):
    """
    Summary page 에 필요한 정보를 가지고 온다.
    """
    # 기업정보
    
    # 애널리스트 의견 
    # 이벤트별 키워드 
    # -> 주가, 주식, 뉴스키워드

    # 종목코드 처리 
    searched_code=str(searched_code).zfill(6) # 005930
    
    # main table 
    company_info=TbName.objects.get(code=searched_code) # TbName object (005930)
    print('#####',company_info)
    # CEO, code, homepage, listed_date, market, market_cap, name, sector, 
    
    # name
    name=TbName.objects.get(code=searched_code).name
    # CEO
    ceo=TbName.objects.get(code=searched_code).CEO
    # market
    market=TbName.objects.get(code=searched_code).market
    # sector
    sector=TbName.objects.get(code=searched_code).sector
    # market_cap
    market_cap=TbName.objects.get(code=searched_code).market_cap
    market_cap=format(market_cap,',')
    
    #listed_date
    listed_date=TbName.objects.get(code=searched_code).listed_date
    listed_date=f'{listed_date}'.format('yyyy-mm-dd')[:11]
  
    
    # tbnews, tbohlcv, tbprofit, tbreport, tbsentimental, tbtradinginfo, updated_date
    
    # comment value # 댓글 반응
    comment_info=TbSentimental.objects.filter(code=searched_code).order_by('-date')[0].comment
    # comment_info=senti_info.order_by('-news_graph')[0] -> newgraph url 됨
    print('### comment_info 결과값:',comment_info)
    # comment value string 인 것들 dict 화
    comment_value=json.loads(comment_info.replace("'", "\""))
    # comment_value.neg : 부정, comment_value.pos : 긍정 
    # print(comment_value)


    # analyst opinion
    a_opinion= TbReport.objects.filter(code=searched_code).order_by('-date')[0].comment


    # OHLCV data 진행예정
    ohlcv_info = TbOHLCV.objects.filter(code=searched_code)
    ohlcv = ohlcv_info.values()
    data={'code':searched_code,'name':name,"market":market,"CEO":ceo,"sector":sector,"market_cap":market_cap,'comment':comment_value,'a_opinion':a_opinion,'ohlcv':ohlcv, 'listed_date':listed_date}
    return render(request,'articleapp/list.html',data)