import scrapy
import requests
from bs4 import BeautifulSoup

class BoardSpider(scrapy.Spider):
    name = 'board'
    start_urls = ['https://finance.naver.com/item/board.naver?code=000270']

    def start_requests(self):
        urls = []
        # 기업 종목코드번호 일단은 기아만!
        company_list = ['000270']

        for company in company_list:
            # 마지막 페이지 찾기
            end_url = f'https://finance.naver.com/item/board.naver?code={company}&page=20000'
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
            response = requests.get(end_url,headers=header)
            soup = BeautifulSoup(response.text,"html.parser")
            end_pages = soup.select_one('td .on a').text
            
            # for page in range(1,int(end_pages)+1):
            # 테스트 page값
            for page in range(1,6):
                try: 
                    url = f'https://finance.naver.com/item/board.naver?code={company}&page={page}'
                    urls.append(url)
                except Exception as e:
                    # print(e)
                    pass

        for url in urls:
            # print(url)
            yield scrapy.Request(url=url, callback=self.crawl_parse)

    def crawl_parse(self,response):
        crawl_urls = []
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
            yield scrapy.Request(url=crawl_url, callback=self.parse_comment)
    def parse_comment(self,response):
        # 타이틀 xpath,css 검색시 빈 리스트 아직 해결x 
        # xpath 한단계씩 들어가보면 tbody부터 빈리스트 출력(table[1]까지 들어갔을땐 값 존재)
        # title = response.xpath('//*[@id="content"]/div[2]/table[1]/tbody/tr[1]/th[1]/strong').extract()   
        # view = response.xpath('//*[@id="content"]/div[2]/table[1]/tbody/tr[1]/th[2]/span').extract()    
        # good = response.xpath('//*[@id="content"]/div[2]/table[1]/tbody/tr[1]/th[2]/strong[1]').extract()
        # bad = response.xpath('//*[@id="content"]/div[2]/table[1]/tbody/tr[1]/th[2]/strong[2]').extract()
        comment = response.xpath('//*[@id="body"]/text()').extract()[0].rstrip()
        print(comment)
        
