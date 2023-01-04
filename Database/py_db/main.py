import pandas as pd
import pymysql
from rdb import MariaDB
from stock_db import stock_db
# from data_df import get_df
import json

if __name__ == '__main__':
    db_config = MariaDB.read_config('db_config')
    mydb = MariaDB(db_config)
    mynews = stock_db(mydb)

    # 종목명, 코드, market
    # kospi_name=pd.read_csv('../data/krx/main.csv',index_col=None,dtype={'code':object,'name':object,'market':int})
    # print(kospi_name.head())
    
    # print('stock_info_insert:', mynews.insert_stock_code(kospi_name))

    # OHLCV
    # OHLCV_kosdaq=pd.read_csv('../data/krx/final_kosdaq_OHLCV.csv',index_col=None,dtype={'code':object,'date':object,'compare_price':float,'open_price':int,'high_price':int,'low_price':int,'close_price':int,'trading_volume':int,'trading_value':int})
    # OHLCV_kospi=pd.read_csv('../data/krx/final_kospi_OHLCV.csv',index_col=None,dtype={'code':object,'date':object,'compare_price':float,'open_price':int,'high_price':int,'low_price':int,'close_price':int,'trading_volume':int,'trading_value':int})

    OHLCV_data=pd.read_csv('../data/krx/fixed_ohlcv.csv',index_col=None,dtype={'code':object,'date':object,'compare_price':float,'open_price':int,'high_price':int,'low_price':int,'close_price':int,'trading_volume':int,'trading_value':int})
    
    # print(OHLCV_kospi)
    # trading_value=pd.concat([OHLCV_kosdaq,OHLCV_kospi],axis=0)
    # trading_value.reset_index(inplace=True)
    # trading_value=trading_value.drop(trading_value.columns[0],axis=1)
    # print(len(trading_value),trading_value.columns)
    # print(trading_value)
    # print('-------------------------------------------')
    OHLCV_data.columns=['date','open_price','high_price','low_price','close_price','trading_volume','trading_value','compare_price','code']
    # print(trading_value)
    print('insert_OHLCV',mynews.insert_OHLCV(OHLCV_data))