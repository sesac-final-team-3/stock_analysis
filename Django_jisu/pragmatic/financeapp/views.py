from django.shortcuts import render

from financeapp.models import TbOHLCV,TbTradingInfo
import time

def finance_data(request,searched_code):
    searched_code=str(searched_code).zfill(6)

    OHLCV_info = TbOHLCV.objects.filter(code=searched_code).order_by('date')
    trading_info = TbTradingInfo.objects.filter(code=searched_code).order_by('date')
    OHLCV_results = OHLCV_info.values()
    trading_results = trading_info.values()
# close_price
    price_list=[]
    for OHLCV_result in OHLCV_results:
        tdate = time.mktime(OHLCV_result['date'].timetuple())*1000

        close_price = OHLCV_result['close_price']
        temp=[tdate,close_price]
        price_list.append(temp)

    vol_institution_list=[]
    vol_retail_investor_list=[]
    vol_foreigner_list=[]

    for trading_result in trading_results:
        tdate = time.mktime(trading_result['date'].timetuple())*1000

        vol_institution = trading_result['vol_institution']
        vol_retail_investor = trading_result['vol_retail_investor']
        vol_foreigner = trading_result['vol_foreigner']

        if vol_institution == None:
            vol_institution = 0
        if vol_retail_investor == None:
            vol_retail_investor = 0
        if vol_foreigner == None:
            vol_foreigner = 0

        temp1=[tdate,vol_institution]
        temp2=[tdate,vol_retail_investor]
        temp3=[tdate,vol_foreigner]

        vol_institution_list.append(temp1)
        vol_retail_investor_list.append(temp2)
        vol_foreigner_list.append(temp3)

    data={'code':searched_code,'price_list':price_list,'vol_institution_list':vol_institution_list,'vol_retail_investor_list':vol_retail_investor_list,
        'vol_foreigner_list':vol_foreigner_list}

    return render(request,'financeapp/list.html', data)