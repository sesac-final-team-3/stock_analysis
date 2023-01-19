from django.shortcuts import render,redirect
from articleapp.models import TbSentimental
from newsapp.models import TbNews
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from articleapp.models import TbName, TbReport, TbSentimental
from financeapp.models import TbOHLCV
import time

def news_graph(request,searched_code:str):
    # Tableau 진행시 
    # graph_info=TbSentimental.objects.filter(code=searched_code).order_by('-news_graph')
    # print('@@@@',graph_info[0].news_graph)
    searched_code=str(searched_code).zfill(6)
    news_table=TbNews.objects.filter(code=searched_code).order_by('-date')[:30]
    # print('!!!!',news_table.values())
    page = request.GET.get('page')
    print('###',page)
    paginator = Paginator(news_table,3)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page=1
        page_obj =paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        page_obj =paginator.page(page)
    
    news_info = TbOHLCV.objects.filter(code=searched_code).order_by('date')
    news_results = news_info.values()
    news_list=[]
    pred_list=[]

    for news_result in news_results:
        tdate = time.mktime(news_result['date'].timetuple())*1000
        
        count = news_result['count']
        pred = news_result['predict']
        if count == None:
            count = 0
        if pred == None:
            pred = 0
        count=int(count)
        try:
            pred=float(pred)
        except:
            if pred[0]=='-':
                pred=  float(pred[1:])*-1
        temp1=[tdate,count]
        temp2=[tdate,pred]
        news_list.append(temp1)
        pred_list.append(temp2)
    print(news_list)
    print(pred_list)
    # print('@@@@',news_table[0].photourl)
    data={'code':searched_code,'news_table':news_table,'page_obj':page_obj,'paginator':paginator,'news_list':news_list,'pred_list':pred_list}

    return render(request,'newsapp/list.html', data)
