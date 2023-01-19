from django.shortcuts import render

from financeapp.models import TbOHLCV,TbTradingInfo
import time

def finance_data(request,searched_code):
    searched_code=str(searched_code).zfill(6)

    OHLCV_info = TbOHLCV.objects.filter(code=searched_code).order_by('date')
    trading_info = TbTradingInfo.objects.filter(code=searched_code).order_by('date')
    OHLCV_results = OHLCV_info.values()
    trading_results = trading_info.values()

    price_list=[]
    BPS_list=[]
    PER_list=[]
    PBR_list=[]
    EPS_list=[]
    DIV_list=[]
    for OHLCV_result in OHLCV_results:
        tdate = time.mktime(OHLCV_result['date'].timetuple())*1000

        close_price = OHLCV_result['close_price']
        temp=[tdate,close_price]
        price_list.append(temp)

        BPS = OHLCV_result['BPS']
        PER = OHLCV_result['PER']
        PBR = OHLCV_result['PBR']
        EPS = OHLCV_result['EPS']
        DIVy = OHLCV_result['DIVy']

        temp5 = [tdate,BPS]
        temp6 = [tdate,PER]
        temp7 = [tdate,PBR]
        temp8 = [tdate,EPS]
        temp9 = [tdate,DIVy]

        BPS_list.append(temp5)
        PER_list.append(temp6)
        PBR_list.append(temp7)
        EPS_list.append(temp8)
        DIV_list.append(temp9)

    vol_institution_list=[]
    vol_retail_investor_list=[]
    vol_foreigner_list=[]

    short_value_list=[]

    
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


        short_value = trading_result['short_value']

        if short_value == None:
            short_value = 0

        temp4 =[tdate,short_value]


        short_value_list.append(temp4)

    print(DIV_list)

    data={'code':searched_code,'price_list':price_list,'vol_institution_list':vol_institution_list,'vol_retail_investor_list':vol_retail_investor_list,
        'vol_foreigner_list':vol_foreigner_list,'short_value_list':short_value_list,'BPS_list':BPS_list,'PER_list':PER_list,'PBR_list':PBR_list,
        'EPS_list':EPS_list,'DIV_list':DIV_list}

    return render(request,'financeapp/list.html', data)