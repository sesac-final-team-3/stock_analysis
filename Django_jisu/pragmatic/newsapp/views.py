from django.shortcuts import render,redirect
from articleapp.models import TbName
from newsapp.models import TbNews
from financeapp.models import TbOHLCV
import time
import json

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def news_graph(request,searched_code:str):
    # code & news name
    searched_code=str(searched_code).zfill(6)
    name = TbName.objects.get(code=searched_code).name
    
  
    # news article
    # news 검색
    news_table=TbNews.objects.filter(code=searched_code).order_by('-date')[:30]
    # new 수 만큼 페이지 생성
    page = request.GET.get('page')
    paginator = Paginator(news_table,3)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page=1
        page_obj =paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        page_obj =paginator.page(page)

    # print('@@@@',news_table[0].photourl)
    data={'code':searched_code,'news_table':news_table,'page_obj':page_obj,'paginator':paginator,'name':name}

    return render(request,'newsapp/list.html', data)
