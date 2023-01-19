import pandas as pd
import numpy as np
import pymysql
from rdb import MariaDB
from stock_db import stock_db
# from data_df import get_df
from datetime import datetime
import json

if __name__ == '__main__':
    db_config = MariaDB.read_config('db_config')
    mydb = MariaDB(db_config)
    mystocks = stock_db(mydb)

    # tb_name
    # main_table=pd.read_csv('../../../workspace/data/krx/final_info.csv',index_col=None)
    # # print(main_table)
    # # print('###',main_table.columns)
    # main_table = main_table.replace({np.nan: None})
    # today=datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    # main_table['updated_date']=today
    # print(main_table)
    # # print(main_table.columns,'####',len(main_table.columns))
    # # print(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
    # print('insert_tb_name',mystocks.insert_stock_info(main_table))

    # # tb_report
    # tb_report_d=pd.read_csv('../../../workspace/data/report/kosdaq_report.csv',index_col=None)
    # tb_report_p=pd.read_csv('../../../workspace/data/report/kospi_report.csv',index_col=None)
    # tb_report_d['code']=tb_report_d['code'].apply(lambda x : str(x).zfill(6))
    # tb_report_p['code']=tb_report_p['code'].apply(lambda x : str(x).zfill(6))
    # tb_report_d.rename(columns={'coment':'comment'},inplace=True)
    # tb_report_p.rename(columns={'coment':'comment'},inplace=True)
    # final_report=pd.concat([tb_report_p,tb_report_d],axis=0)
    # final_report.reset_index(inplace=True)
    # final_report=final_report.drop(final_report.columns[0],axis=1)
    # print('insert_tb_report',mystocks.insert_report(final_report))

    # 종목명, 코드, market
    # kospi_name=pd.read_csv('../data/krx/main.csv',index_col=None,dtype={'code':object,'name':object,'market':int})
    # print(kospi_name.head())    
    # print('stock_info_insert:', mynews.insert_stock_code(kospi_name))

    # OHLCV
    # OHLCV_data=pd.read_csv('../../../workspace/data/krx/fixed_ohlcv.csv',index_col=None,dtype={'code':object,'date':object,'compare_price':float,'open_price':int,'high_price':int,'low_price':int,'close_price':int,'trading_volume':int,'trading_value':int})
    # OHLCV_data.columns=['date','open_price','high_price','low_price','close_price','trading_volume','trading_value','compare_price','code']
    # print(len(OHLCV_data['code'].unique()))
    # print('insert_OHLCV',mystocks.insert_OHLCV(OHLCV_data))

    # OHLCV_2
#     o_df=pd.read_csv('../../../workspace/data/krx/bb.csv',index_col=False,low_memory=False)
#     o_df['code']=o_df['code'].apply(lambda x : str(x).zfill(6))
#     # print(json.loads(o_df['news_keyword'][0].replace("'", '"')))
#     # o_df['news_keyword']=o_df['news_keyword'].apply(lambda x : json.loads(x.replace("'", '"')) if type(x) == str else None)
#     # o_df['news_keyword']=o_df['news_keyword'].apply(lambda x : '\t'.join([x[k].replace(',', '_') for k in x]) if type(x) == dict else None)
#     # print(o_df[o_df['code']=='373220']['news_keyword'])
#     o_df['updated_date']=datetime.today().strftime("%Y/%m/%d %H:%M:%S")
#     o_df = o_df.replace({np.nan: None})
#     print('insert_OHLCV',mystocks.insert_OHLCV(o_df[o_df['code']=='373220']))
# #  ['2022-02-11', '373220', "{'부정_단어': '외국인,기관,상승,매수,전날,상승세,한국,지난해,상장,이틀', '부정_빈도': '0.26,0.16,0.16,0.16,0.16,0.16,0.16,0.16,0.11,0.11', '긍정_단어': '종목,상승,외국인,리츠,금융,지주,작년,매도,다만,하락', '긍정_빈도': '0.33,0.33,0.33,0.22,0.22,0.22,0.22,0.22,0.22,0.22'}", 463500.0, 484000.0, 457000.0, 482000.0, 1411055.0, 672692384000.0, 1.58, 34398.0, 0.0, 14.01, 0.0, 0.0, 0.0, '2023/01/12 17:18:31']
# @@@@@@ INSERT INTO tb_ohlcv(date,code,news_keyword,open_price,high_price,low_price,close_price,trading_volume,trading_value,compare_price,BPS,PER,PBR,EPS,DIV,DPS,updated_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);

    # OHLCV_3
    # o_df=pd.read_csv('../../../workspace/data/krx/real_ohlcv.csv',index_col=False,dtype=object)
    # # o_df=pd.read_csv('../../../workspace/data/krx/a_text.csv',index_col=False,dtype=object)
    # print('#####o_df를 불러왔습니다.')
    # o_df['code']=o_df['code'].apply(lambda x : str(x).zfill(6))
    # o_df['updated_date']=datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    # o_df=o_df.replace({np.nan:None})
    # # print(o_df['code'].head())
    # # print(o_df.iloc[:,8:].head())
    # # print(o_df.iloc[:,8:].tail())
    # print('insert_OHLCV',mystocks.insert_OHLCV(o_df))

    # trading_info
    o_df=pd.read_csv('../../../workspace/data/krx/final_tradingINFO.csv',index_col=False,dtype=object)
    print('#####trading_info_df를 불러왔습니다.')
    o_df['code']=o_df['code'].apply(lambda x : str(x).zfill(6))
    o_df['updated_date']=datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    o_df=o_df.replace({np.nan:None})
    # print(o_df['code'].head())
    # print(o_df.iloc[:,8:].head())
    # print(o_df.iloc[:,8:].tail())
    print('insert_tradinginfo',mystocks.insert_tradinginfo(o_df))