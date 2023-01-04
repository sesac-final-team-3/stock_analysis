import pandas as pd
import pymysql
from rdb import MariaDB


class stock_db:
    '''
    final db src 
    '''
    def __init__(self, db:MariaDB) -> None:
        self.db = db
        
    def insert_stock_code(self, df:pd.DataFrame) -> bool:
        '''
        종목 관련 데이터 프레임을 통해 데이터베이스에 종목 정보를 삽입합니다. 
        '''
        # 데이터프레임 drop_duplicates()해서 df에 적용
        # df.drop_duplicates(subset='URL',inplace=True) # 중복제거
        # df.fillna('', inplace=True) # TypeError: replace() argument 1 must be str, not float
        print('### 종목관련 (code, name, market)에 대한 정보가 들어 왔습니다.')
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

        return self.db.insert_many('tb_ohlcv', ','.join(df.columns), df.values.tolist()) # 성공, 실패

    # # 둘 중 하나를 사용
    # # def select_news(self, url_list:list) -> dict:
    # def select_news(self, df:pd.DataFrame) -> dict:
    #     '''
    #     뉴스 데이터를 검색하여 ID, URL값을 반환합니다.
    #     '''
    #     # select query 작성
    #     # 가져올 값 - id, url
    #     # WHERE - IN
    #     url_list = df['URL'].tolist()
    #     sql_query = '''SELECT ID, URL
    #     FROM tb_news
    #     WHERE URL IN ("{}")
    #     '''.format('", "'.join(url_list))
    #     # self.db.DB.
    #     with self.db.DB.cursor() as cur:
    #         cur.execute(sql_query)
    #         datas = cur.fetchall()

    #     news_dict = {}
    #     for news_id, url in datas:
    #         news_dict[url] = news_id

    #     return news_dict # {url: id} dictionary
    
    # def insert_user(self, df:pd.DataFrame) -> bool:
    #     '''
    #     유저정보를 삽입합니다.
    #     '''
    #     df = df.drop_duplicates(subset='UserID',keep='last')
        
    #     error_list=[]
    #     try:
    #         df['DomainID'] = df['URL'].apply(lambda x : 1 if 'naver' in x else 2)
    #         df = df[['DomainID', 'UserID','UserName']]
    #         df.fillna('', inplace=True)
    #         columns = df.columns
    #         value=list(df.itertuples(index=False, name=None))
    #         sql_qr = f"INSERT INTO tb_user({','.join(columns)}) " \
    #             "VALUES (" +','.join(["%s"]*len(value[0])) + ") on DUPLICATE KEY UPDATE UserID=UserID;"
            
    #         with self.db.DB.cursor() as cur:
    #             cur.executemany(sql_qr, value)
    #             datas = self.db.DB.commit()

    #         return True

    #     except Exception as e:
    #         import traceback
    #         traceback.print_exc()
    #         # print(e)
    #         return False

    
    # def select_user(self, df:pd.DataFrame) -> dict:
    #     '''
    #     모든 유저 정보를 가져옵니다.
    #     {
    #         'UserID': { ID: , DomainID: , UserName: },
    #     }
    #     '''

    #     UserID_list = df['UserID'].tolist()
    #     sql_query = '''SELECT UserID, ID, DomainID, UserName FROM tb_user
    #     WHERE UserID IN ("{}")
    #     '''.format('","'.join(map(str, UserID_list)))

    #     with self.db.DB.cursor() as cur:
    #         cur.execute(sql_query)
    #         datas = cur.fetchall()

    #     userID_dict = {}
    #     for UserID, ID, DomainID, UserName in datas:
    #         userID_dict[UserID] = {'ID':ID, 'DomainID':DomainID, 'UserName':UserName}
        
    #     return userID_dict 

    # def insert_comments(self, df:pd.DataFrame, news_dict, user_json) -> bool:
    #     '''
    #     댓글 데이터를 삽입합니다.
    #     df : comment_df
    #     '''

    #     # WritedAt 포맷 변경 (%Y-%m-%d %H:%M:%S)
    #     df['WritedAt'] = pd.to_datetime(df['WritedAt']) if 'WritedAt' in df.columns else ''
    #     df['check'] = df['URL'].apply(lambda x: x in news_dict)
    #     df = df[df['check'] == True]
    #     df.fillna('', inplace=True)
    #     df.reset_index(inplace=True)
    #     df['NewsID'] = df['URL'].apply(lambda x : news_dict[x] if x in news_dict else None)
    #     df.dropna(inplace=True)
    #     df.reset_index(inplace=True)
    #     df['UserID'] = df['UserID'].apply(lambda x: user_json[str(x)]['ID'])

    #     #db에 적재할 최종 데이터프레임
    #     df=df[['NewsID','UserID','WritedAt','Content']]
    #     value=list(df.itertuples(index=False, name=None))

    #     try:
    #         sql = '''insert into tb_comment(NewsID,UserID,WritedAt,Content) 
    #         values(%s,%s,%s,%s);'''  

    #         with self.db.DB.cursor() as cur:
    #             cur.executemany(sql, value)
    #             self.db.DB.commit()

    #     except Exception as e:
    #         return print('db insert 실패',e)


        
        