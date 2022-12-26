import scrapy
import requests
from bs4 import BeautifulSoup
from boardcomment.items import BoardcommentItem
import pandas as pd

class BoardSpider(scrapy.Spider):
    name = 'board'
    start_urls = ['https://finance.naver.com/item/board.naver?code=000270']
   
    def start_requests(self):
        urls = []
        # company_df = pd.read_csv('C:/Users/seon/Desktop/stock_analysis/Data/kospi200.csv')
        # company_list = company_df.iloc[:,1]
        # 코스피 "005930","000270,"373220","207940","000660","006400","051910""
        company_list = ["005380","035420","068270"]
        # 코스닥 
        # company_list = ["091990","247540","066970","263750","293490","112040","028300","278280","035760","058470"]
        for company in company_list:

            # 마지막 페이지 찾기
            end_url = f'https://finance.naver.com/item/board.naver?code={company}&page=100000'
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
            response = requests.get(end_url,headers=header)
            soup = BeautifulSoup(response.text,"html.parser")
            end_pages = soup.select_one('td .on a').text
            # print(end_url)
            # print(int(end_pages.replace(',',''))+1)
            # print(response)
            for page in range(1,int(end_pages.replace(',',''))+1):
                # print(page)
            # 테스트 page값
            # for page in range(1,2):
                try: 
                    url = f'https://finance.naver.com/item/board.naver?code={company}&page={page}'
                    urls.append([f'{company}', url])
                    print(url)
                except Exception as e:
                    print(e)
                    pass

        for com_code, url in urls:
            # print(url)
            yield scrapy.Request(url=url, callback=self.crawl_parse, meta={'com_code':com_code})

    def crawl_parse(self,response):
        crawl_urls = []
        com_code = response.meta['com_code']
        # print(response)
        for i in range(3,26):
            try:
                param = response.xpath(f'//*[@id="content"]/div[2]/table[1]/tbody/tr[{i}]/td[2]/a/@href').extract()[0]
                page_url = 'https://finance.naver.com' + param
                # print(page_url)
                crawl_urls.append(page_url)
            except Exception as e:
                # print(e)
                pass
        for crawl_url in crawl_urls:
            print(crawl_url)
            yield scrapy.Request(url=crawl_url, callback=self.parse_comment, meta={'com_code':com_code})

    def parse_comment(self,response):
        item = BoardcommentItem()

        com_code = response.meta['com_code']
        title = response.xpath('//*[@id="content"]/div[2]/table[1]/tr[1]/th[1]/strong/text()').extract()[0]   
        view = response.xpath('//*[@id="content"]/div[2]/table[1]/tr[1]/th[2]/span/text()').extract()[0]   
        recommend = response.xpath('//*[@id="content"]/div[2]/table[1]/tr[1]/th[2]/strong[1]/text()').extract()[0] 
        decommend = response.xpath('//*[@id="content"]/div[2]/table[1]/tr[1]/th[2]/strong[2]/text()').extract()[0] 
        temp_comment = response.xpath('//*[@id="body"]/text()').extract()
        date = response.xpath('//*[@id="content"]/div[2]/table[1]/tr[2]/th[2]/text()').extract()[0]
        for i in range(len(temp_comment)):
            temp_comment[i]=temp_comment[i].rstrip()
        comment = '\n'.join(temp_comment)

        item['title'] = title
        item['view'] = view
        item['recommend'] = recommend
        item['decommend'] = decommend
        item['comment'] = comment
        item['date'] = date
        item['com_code'] = com_code

        yield item
