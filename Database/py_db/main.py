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