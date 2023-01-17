from django.shortcuts import render,HttpResponse
from .models import TbName,TbSentimental,TbReport
from finance.models import TbOHLCV
import time
import json
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def searching_db(request):
    """
    searching에서 받은 code 조회
    """
    print('###convert 접속')
    searching=request.POST.get('stock_search')
    print('@@@',searching)
    company_info=TbName.objects.filter(name=searching)
    searched_code = str(company_info.values()[0]['code'])
    print(f'{searched_code}를 검색합니다.')
    return redirect('summary:summary_result',searched_code)

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
    # listed_date
    listed_date=TbName.objects.get(code=searched_code).listed_date
    # sector
    sector=TbName.objects.get(code=searched_code).sector
    # market_cap
    market_cap=TbName.objects.get(code=searched_code).market_cap
    market_cap=format(market_cap,',')
    
    
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
    
    # OHLCV data 진행예정 , ['date':date,(parsing한 시간으로 ) 'close_price':13234, up: ['긍정,'부정'],down:['부정']]
    ohlcv_info = TbOHLCV.objects.filter(code=searched_code).order_by('date')
    ohlcv = ohlcv_info.values()
    ohlcv_list=[]
    
    for ohlcv_result in ohlcv:
        
        temp={}
        temp['x']=time.mktime(ohlcv_result['date'].timetuple())*1000
        temp['y']=int(ohlcv_result['close_price'])
        temp['compare_price']=str(ohlcv_result['compare_price'])
        
        if ohlcv_result['news_keyword']==None:
            temp['word']={'긍정_단어':'없음','부정_단어':'없음'}
        else:
            keyword_json=json.loads(ohlcv_result['news_keyword'].replace("'", "\""))
            temp['word']=keyword_json

        # {'x': 1668470400.0, 'y': 596000, 'compare_price': '-1.32', 'word': {'부정_단어': '개인,증시,상승,미국,매수,발언,전날,의장,매도,성장', '부정_빈도': '0.31,0.31,0.25,0.25,0.19,0.19,0.19,0.19,0.19,0.19', '긍정_단어': '기관,외국인,상위,전자,매수,투자,관련,주의,올해,기간', '긍정_빈도': '0.6,0.4,0.4,0.4,0.4,0.2,0.2,0.2,0.2,0.2'}},
        ohlcv_list.append(temp)
        print(ohlcv_list)
        
        # "{'부정_단어': '매수,상승,주식,전자,구매,종목,기준,환율,신청,전체', '부정_빈도': '0.31,0.25,0.25,0.25,0.25,0.25,0.25,0.19,0.19,0.19', '긍정_단어': '상승,개인,생산,환율,기관,종목,협력,인도네시아,공급,배터리', '긍정_빈도': '0.25,0.25,0.19,0.19,0.19,0.19,0.12,0.12,0.12,0.12'}"
    
    data={'code':searched_code,'name':name,"market":market,"ceo":ceo,"listed_date":listed_date,"sector":sector,"market_cap":market_cap,'comment':comment_value,'a_opinion':a_opinion,'ohlcv_list':ohlcv_list}
    return render(request,'test.html',data)

#  TbOHLCV.objects.filter(code="373220").values()[0]
# Out[44]: 
# {'id': 226,
#  'date': datetime.datetime(2022, 1, 28, 0, 0, tzinfo=datetime.timezone.utc),
#  'code_id': '373220',
#  'compare_price': -10.89,
#  'open_price': 476000,
#  'high_price': 483000,
#  'low_price': 445000,
#  'close_price': 450000,
#  'trading_volume': 4559773,
#  'trading_value': 2104994467000,
#  'news_keyword': "{'부정_단어': '상장,하락,기관,매도,종목,연구원,시가총액,외국인,삼성,증시', '부정_빈도': '0.22,0.17,0.16,0.14,0.14,0.14,0.12,0.12,0.12,0.1', '긍정_단어': '하락,상장,하루,사업,증시,시가총액,자금,헤럴드경제,기준,투자', '긍정_빈도': '0.33,0.2,0.2,0.2,0.13,0.13,0.13,0.13,0.13,0.13'}",
#  'BPS': 34398.0,
#  'PER': 0.0,
#  'PBR': 13.08,
#  'EPS': 0.0,
#  'DIVy': 0.0,
#  'DPS': 0.0,
#  'updated_date': datetime.datetime(2023, 1, 13, 13, 45, 33, tzinfo=datetime.timezone.utc)}
