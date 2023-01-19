import pandas as pd
import pymysql
from rdb import MariaDB


class stock_db:
    '''
    final db src 
    '''
    def __init__(self, db:MariaDB) -> None:
        self.db = db
        

    def insert_stock_info(self, df:pd.DataFrame) -> bool:

        '''
        종목 관련 데이터 프레임을 통해 데이터베이스에 종목 정보를 삽입합니다. 
        '''
        # 데이터프레임 drop_duplicates()해서 df에 적용
        # df.drop_duplicates(subset='URL',inplace=True) # 중복제거
        # df.fillna('', inplace=True) # TypeError: replace() argument 1 must be str, not float 
        print('### 종목관련 (code, name, market,sector, listed_date, CEO, homepage , market_cap)에 대한 정보가 들어 왔습니다.')
        columns = df.columns
        
        df.reset_index(inplace=True)
        df = df[columns]

        return self.db.insert_many('tb_name', ','.join(df.columns), df.values.tolist()) # 성공, 실패

    def insert_OHLCV(self, df:pd.DataFrame) -> bool:
        '''
        종목 OHLCV 관련 데이터 프레임을 통해 데이터베이스에 OHLCV 를 삽입합니다. 
        '''
        # 데이터프레임 drop_duplicates()해서 df에 적용
        # df.drop_duplicates(subset='URL',inplace=True) # 중복제거
        # df.fillna('', inplace=True) # TypeError: replace() argument 1 must be str, not float
        print('### 종목관련 OHLCV 에 대한 정보가 들어 왔습니다.')
        columns = df.columns
        df.reset_index(inplace=True)
        df = df[columns]
        # for c in columns:
        #     df[c] = df[c].apply(lambda x : x.replace('\'', '') if type(x)==str else None)
        return self.db.insert_many('tb_ohlcv', ','.join(df.columns), df.values.tolist()) # 성공, 실패

    def insert_report(self, df:pd.DataFrame) -> bool:
        '''
        종목 report 관련 데이터 프레임을 통해 데이터베이스에 report 를 삽입합니다. 
        '''
        # 데이터프레임 drop_duplicates()해서 df에 적용
        # df.drop_duplicates(subset='URL',inplace=True) # 중복제거
        # df.fillna('', inplace=True) # TypeError: replace() argument 1 must be str, not float
        print('### 종목관련 report 에 대한 정보가 들어 왔습니다.')
        columns = df.columns
        df.reset_index(inplace=True)
        df = df[columns]

        return self.db.insert_many('tb_report', ','.join(df.columns), df.values.tolist()) # 성공, 실패

    def insert_tradinginfo(self, df:pd.DataFrame) -> bool:
        '''
        종목 report 관련 데이터 프레임을 통해 데이터베이스에 report 를 삽입합니다. 
        '''
        # 데이터프레임 drop_duplicates()해서 df에 적용
        # df.drop_duplicates(subset='URL',inplace=True) # 중복제거
        # df.fillna('', inplace=True) # TypeError: replace() argument 1 must be str, not float
        print('### 종목관련 report 에 대한 정보가 들어 왔습니다.')
        columns = df.columns
        df.reset_index(inplace=True)
        df = df[columns]

        return self.db.insert_many('tb_tradinfo', ','.join(df.columns), df.values.tolist()) # 성공, 실패

