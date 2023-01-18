from django.shortcuts import render
from articleapp.models import TbSentimental
from newsapp.models import TbNews

def finance_data(request,searched_code):
    # # Tableau 진행시 
    # graph_info=TbSentimental.objects.filter(code=searched_code).order_by('-news_graph')
    # # print('@@@@',graph_info[0].news_graph)
    print('@@@@@@@',searched_code)
    data={'code':searched_code}

    return render(request,'financeapp/list.html', data)