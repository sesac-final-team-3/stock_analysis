from django.shortcuts import render,redirect
from articleapp.models import TbSentimental
from newsapp.models import TbNews

def news_graph(request,searched_code):
    # Tableau 진행시 
    graph_info=TbSentimental.objects.filter(code=searched_code).order_by('-news_graph')
    # print('@@@@',graph_info[0].news_graph)

    news_table=TbNews.objects.filter(code=searched_code).order_by('date')[:3]
    # print('!!!!',news_table.values())
    # print(news_table.values())
    data={'code':searched_code,'news_table':news_table}
    paginate_by=3
    return render(request,'newsapp/list.html', data)