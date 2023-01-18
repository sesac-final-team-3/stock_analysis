from django.shortcuts import render,redirect
from articleapp.models import TbSentimental
from newsapp.models import TbNews
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def news_graph(request,searched_code):
    # Tableau 진행시 
    graph_info=TbSentimental.objects.filter(code=searched_code).order_by('-news_graph')
    # print('@@@@',graph_info[0].news_graph)

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

    print('@@@@',news_table[0].photourl)
    data={'code':searched_code,'news_table':news_table,'page_obj':page_obj,'paginator':paginator}

    return render(request,'newsapp/list.html', data)
