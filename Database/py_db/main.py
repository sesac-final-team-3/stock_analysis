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

    # 종목명, 코드, market
    # kospi_name=pd.read_csv('../data/krx/main.csv',index_col=None,dtype={'code':object,'name':object,'market':int})
    # print(kospi_name.head())
    
    # print('stock_info_insert:', mynews.insert_stock_code(kospi_name))

    # OHLCV
    # OHLCV_data=pd.read_csv('../data/krx/fixed_ohlcv.csv',index_col=None,dtype={'code':object,'date':object,'compare_price':float,'open_price':int,'high_price':int,'low_price':int,'close_price':int,'trading_volume':int,'trading_value':int})

    # trading_value=pd.concat([OHLCV_kosdaq,OHLCV_kospi],axis=0)
    # trading_value.reset_index(inplace=True)
    # trading_value=trading_value.drop(trading_value.columns[0],axis=1)
    
    # print('-------------------------------------------')
    # OHLCV_data.columns=['date','open_price','high_price','low_price','close_price','trading_volume','trading_value','compare_price','code']
    

    # print('insert_OHLCV',mynews.insert_OHLCV(OHLCV_data))

    # tb_name
    main_table=pd.read_csv('../../../workspace/data/krx/final_info.csv',index_col=None)
    # print(main_table)
    # print('###',main_table.columns)


    main_table = main_table.replace({np.nan: None})
    today=datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    main_table['updated_date']=today
    print(main_table)
    # print(main_table.columns,'####',len(main_table.columns))
    # print(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
    print('insert_tb_name',mystocks.insert_stock_info(main_table))