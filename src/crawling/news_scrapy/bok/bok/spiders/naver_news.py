import scrapy
import datetime
import re
from bok.items import NaverNews
from ..middlewares import TooManyRequestsRetryMiddleware
import time
import pandas as pd
import logging
# from fake_useragent import UserAgent


class NaverNewsSpider(scrapy.Spider):
    name = 'naver_news'
    start_urls = ['http://search.naver.com/']
    crawled_url = []
    custom_settings = {
        'DOWNLOADER_CLIENTCONTEXTFACTORY': 'bok.contextfactory.LegacyConnectContextFactory',
    }

    def start_requests(self):
        # start_date = ' 20221215'
        end_date = '20221130'
        search_day = ' 20221101'
        self.retry_url = []
        url_list = []
        while True:
            if int(search_day) <= int(end_date):
                # 1001 : 연합뉴스
                # 1018 : 이데일리
                # 2227 : 연합인포맥스
                # 1011 : 서울경제
                # 1016 : 헤럴드 경제
                # 2254 : 더 벨
                # 1009 : 매일경제
                for news_company in ['1001', '1018', '2227', '1011', '1016', '2254', '1009']:
                    # url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds={0}&de={1}&news_office_checked={2}&docid=&nso=so:dd,p:,a:all&mynews=1&start=1&refresh_start=0'.format(
                    #     search_day, searc
                    #
                    #
                    # h_day, news_company)
                    url = 'https://search.naver.com/search.naver?&where=news&query=현대차&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds={0}&de={1}&news_office_checked={2}&docid=&nso=so:dd,p:,a:all&mynews=1&start=1&refresh_start=0'.format(
                        search_day, search_day, news_company)
                    # print(url, search_day)
                    url_list.append([url, search_day])
            else:
                break
            search_day = pd.to_datetime(search_day) + datetime.timedelta(days=1)
            search_day = search_day.strftime('%Y%m%d')
        for urls, se_date in url_list:
            yield scrapy.Request(url=urls,
                                 meta={'date': se_date},
                                 callback=self.parse_news)

    def parse_news(self, response):
        # self.logger.critical(response.url)
        # ua = UserAgent(verify_ssl=False)
        if response.url not in self.crawled_url:
            self.crawled_url.append(response.url)
            articles = response.xpath('//*[@id="main_pack"]/section/div/div[2]/ul/li')

            for article in articles:
                if article.xpath('./div/div/div[1]/div[2]/a[1]/text()') != []:
                    media = article.xpath('./div/div/div[1]/div[2]/a[1]/text()').get()
                    # 네이버뉴스 여부
                    if article.xpath('./div[1]/div/div[1]/div[2]/a[2]/text()') != []:
                        naver = article.xpath('./div[1]/div/div[1]/div[2]/a[2]/text()').get()
                    else:
                        naver = ''
                else:
                    media = ''
                    naver = ''

                if naver == '네이버뉴스':
                    page_url = article.xpath('./div[1]/div/div[1]/div[2]/a[2]/@href').get()
                    cur_date = response.meta['date']
                    page_url_fake_user = page_url
                elif article.xpath('./div/div/a/@href') != []:
                    page_url = article.xpath('./div/div/a/@href').get()
                    cur_date = response.meta['date']
                    page_url_fake_user = page_url
                    # 더벨 디버깅
                    if media == '더벨':
                        url_id = page_url_fake_user.split('key=')[-1].split('&')[0]
                        page_url_fake_user = f'http://www.thebell.co.kr/free/content/ArticleView.asp?key={url_id}&svccode=00&page=1&sort=thebell_check_time'
                        # print(media, page_url_fake_user)
                    else:
                        pass

                if media != '':
                    print(media, '네이버 : ', naver, '/', page_url_fake_user)
                    yield scrapy.Request(
                        page_url_fake_user,
                        callback=self.parse_page,
                        # headers={
                        #     'User-Agent': ua.random},
                        meta={"media": media, "date": cur_date, 'url': page_url_fake_user, 'naver': naver},
                    )

        next_page = response.xpath('//*[@id="main_pack"]/div[2]/div/a[2]/@href')
        if next_page != []:
            yield response.follow(
                next_page[-1].get(),
                meta={'date': cur_date},
                callback=self.parse_news)

    def parse_page(self, response):
        logging.info("response.status:%s" % response.status)
        logourl = response.selector.css('div.main-nav__logo img').xpath('@src').extract()
        logging.info('response.logourl:%s' % logourl)
        item = NaverNews()
        item["media"] = response.meta["media"]
        item["date"] = response.meta["date"]
        item["url"] = response.meta["url"]
        naver = response.meta['naver']
        if naver == '네이버뉴스':
            content = response.xpath('//*[@id="contents"]/text()')
            if content != []:
                content = response.xpath('//*[@id="dic_area"]/text()').extract()
                title = response.xpath('//*[@id="title_area"]/span/text()').get()
            else:
                content = response.xpath('//*[@id="contents"]/text()').extract()
            if response.xpath('//*[@class="nbd_im_w _LAZY_LOADING_WRAP "]/div/img') != []:
                photourl = response.xpath('//*[@class="nbd_im_w _LAZY_LOADING_WRAP "]/div/img/@data-src').getall()
            elif response.xpath('//*[@id="img1"]/@data-src') != []:
                photourl = response.xpath('//*[@id="img1"]/@data-src').getall()
            else:
                photourl = ''
            date_hour = response.xpath('//*[@id="ct"]/div[1]/div[3]/div[1]/div[1]/span/@data-date-time').get()
            item["date_hour"] = date_hour
        elif item["media"] == "연합인포맥스":
            photo_base = 'https://news.einfomax.co.kr/'
            # time.sleep(0.2)
            title = response.xpath('//*[@id="user-container"]/div[3]/header/div/div/text()').get()
            # 인포맥스 본문 양식
            content = response.xpath('//*[@id="article-view-content-div"]/text()').getall()
            re_content = ' '.join([re.sub('[^a-zA-Z가-힣ㄱ-ㅎ0-9., ]', '', cnt).strip() for cnt in content]).strip()
            if response.xpath('//*[@id="article-view-content-div"]/div/figure/img/@src') != []:
                photourl = photo_base + response.xpath(
                    '//*[@id="article-view-content-div"]/div/figure/img/@src').getall()
            else:
                photourl = ''
            if re_content == '':
                if response.xpath('//*[@id="article-view-content-div"]/p/text()') != []:
                    content = response.xpath('//*[@id="article-view-content-div"]/p/text()').getall()
                    if response.xpath(
                            '//*[@id="article-view-content-div"]/div/figure/img/@src') != []:
                        photourl = photo_base + response.xpath(
                            '//*[@id="article-view-content-div"]/div/figure/img/@src').getall()
                    else:
                        photourl = ''
                else:
                    content = 'retry'
            date_hour = response.xpath(
                '//*[@id="user-container"]/div[3]/header/section/div/ul/li[2]/text()').get().split('승인 ')[-1]
            item["date_hour"] = date_hour

        elif item["media"] == "이데일리":
            # 이데일리 카타르 배너 디버깅
            if response.xpath('//*[@id="contents"]/section[1]/section[1]/div[1]/div[1]/h2/text()') != []:
                title = response.xpath('//*[@id="contents"]/section[1]/section[1]/div[1]/div[1]/h2/text()').get()
                content = response.xpath(
                    '//*[@id="contents"]/section[1]/section[1]/div[1]/div[3]/div[1]/text()').getall()
                photourl = response.xpath(
                    '//*[@id="contents"]/section[1]/section[1]/div[1]/div[3]/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/img/@src').getall()
            elif response.xpath('//*[@id="swiper_main"]/div[1]/div[1]/h2/text()') != []:
                title = response.xpath('//*[@id="swiper_main"]/div[1]/div[1]/h2/text()').get()
                content = response.xpath('//*[@id="swiper_main"]/div[1]/div/text()').getall()
                photourl = response.xpath(
                    '//*[@id="contents"]/section[1]/section[1]/div[1]/div[3]/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/img/@src').getall()
            else:
                content = 'retry'

        # elif item["media"] == "한국경제":
        #     # 한국경제
        #     if response.xpath('//*[@id="container"]/div/div/article/h1/text()') != []:
        #         title = response.xpath('//*[@id="contents"]/article/div/div[1]/div[1]/h1/text()').get()
        #         content = response.xpath('//*[@id="contents"]/article/div/div[1]/div[2]/div[1]/text()').getall()
        #     # 한국경제 산업
        #     elif response.xpath('//*[@id="container"]/div/div/article/h1') != []:
        #         title = response.xpath('//*[@id="container"]/div/div/article/h1/text()').get()
        #         content = response.xpath('//*[@id="articletxt"]/text()').getall()
        #     else:
        #         content = 'retry'
        elif item["media"] == "매일경제":
            # 매일경제
            if response.xpath('//*[@id="container"]/section/div[2]/section/div/div/div/h2/text()') != []:
                title = response.xpath('//*[@id="container"]/section/div[2]/section/div/div/div/h2/text()').get()
                content = response.xpath(
                    '//*[@id="container"]/section/div[3]/section/div[1]/div[1]/div[1]/text()').getall()
                re_content = ' '.join([re.sub('[^a-zA-Z가-힣ㄱ-ㅎ0-9., ]', '', cnt).strip() for cnt in content]).strip()
                # 다른 html 디버깅
                if re_content != '':
                    pass
                else:
                    content = response.xpath(
                        '//*[@id="container"]/section/div[3]/section/div[1]/div[1]/div[1]/p/text()').getall()
                photourl = response.xpath(
                    '//*[@id="container"]/section/div[3]/section/div[1]/div[1]/div[1]/div/figure/div/img/@src').getall()
            # 매경모바일
            elif response.xpath('//*[@id="container"]/section/div[1]/section/div/div/div/h2/text()') != []:
                title = response.xpath('//*[@id="container"]/section/div[1]/section/div/div/div/h2/text()').get()
                content = response.xpath(
                    '//*[@id="container"]/section/div[2]/section/div/div[1]/div[1]/text()').getall()
                photourl = response.xpath(
                    '//*[@id="container"]/section/div[3]/section/div[1]/div[1]/div[1]/div/figure/div/img/@src').getall()
            else:
                content = 'retry'

        elif item["media"] == "더벨":
            # print(item["media"], item["url"])
            # 더 벨
            if response.xpath('//*[@id="contents"]/div[3]/div/div[1]/div/div[3]/div[1]/p/text()') != []:
                title = response.xpath('//*[@id="contents"]/div[3]/div/div[1]/div/div[3]/div[1]/p/text()').getall()
                title = ''.join(title)
                content = response.xpath('///*[@id="article_main"]/text()').getall()
                photourl = response.xpath('/html/body/div[3]/div[3]/div/div/div/div/div/div/figure/img/@src').getall()
            else:
                content = 'retry'
            date_hour = response.xpath(
                '//*[@id="contents"]/div[3]/div/div[1]/div/div[3]/div[1]/div[1]/span[2]/text()').get().split('공개 ')[-1]
            item["date_hour"] = date_hour
        elif item["media"] == "헤럴드경제":
            # 헤럴드경제
            if response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/ul/li[2]/text()') != []:
                title = response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/ul/li[2]/text()').get()
                if response.xpath('//*[@id="articleText"]/p/text()') != []:
                    content = response.xpath('//*[@id="articleText"]/p/text()').getall()
                else:
                    content = response.xpath('//*[@id="articleText"]/text()').getall()
                photourl = response.xpath('//*[@id="articleText"]/table/tbody/tr/td/img/@src').getall()
            else:
                content = 'retry'

        elif item["media"] == "서울경제":
            # 서울경제
            if response.xpath('//*[@id="v-left-scroll-in"]/div[1]/h1/text()') != []:
                title = response.xpath('//*[@id="v-left-scroll-in"]/div[1]/h1/text()').get()
                # if response.xpath('//*[@id="v-left-scroll-in"]/div[2]/div[1]/div[2]/text()') != []:
                content = response.xpath('//*[@id="v-left-scroll-in"]/div[2]/div[1]/div/text()').getall()
                # else:
                #     content = response.xpath('//*[@id="v-left-scroll-in"]/div[2]/div[1]/div[1]/text()').getall()
            # 서울경제 모바일
                photourl = response.xpath('//*[@id="v-left-scroll-in"]/div[2]/div[1]/div[2]/figure/p/img/@src').getall()
            elif response.xpath('//*[@id="contentArea"]/div[1]/div[1]/div/div[1]/h1') != []:
                title = response.xpath('//*[@id="contentArea"]/div[1]/div[1]/div/div[1]/h1').get()
                content = response.xpath('//*[@id="contentArea"]/div[1]/div[1]/div/div[3]/text()').getall()
                photourl = response.xpath('//*[@id="v-left-scroll-in"]/div[2]/div[1]/div[2]/figure/p/img/@src').getall()
            else:
                content = 'retry'

        else:
            # 연합뉴스
            if 'naver' in response.url:
                title = response.xpath('//*[@id="ct"]/div[1]/div[2]/h2/text()').get()
                content = response.xpath('//*[@id="dic_area"]/text()').getall()
                photourl = response.xpath('//*[@id="articleWrap"]/div[2]/div/div/article/div/figure/div/span/img/@src')
            # 연합뉴스 앱
            elif response.xpath('//*[@id="articleWrap"]/div[1]/header/h1/text()') != []:
                title = response.xpath('//*[@id="articleWrap"]/div[1]/header/h1/text()').get()
                content = response.xpath('//*[@id="articleWrap"]/div[2]/div/div/article/p/text()').getall()
                photourl = response.xpath('//*[@id="articleWrap"]/div[2]/div/div/article/div/figure/div/span/img/@src')
            # 연합뉴스 모바일 선택
            elif response.xpath('//*[@id="articleWrap"]/header/h1/text()') != []:
                title = response.xpath('//*[@id="articleWrap"]/header/h1/text()').get()
                content = response.xpath('//*[@id="articleWrap"]/div/p/text()').getall()
                photourl = response.xpath('//*[@id="articleWrap"]/div[2]/div/div/article/div/figure/div/span/img/@src')
            else:
                content = 'retry'

        re_content = ' '.join([re.sub('[^a-zA-Z가-힣ㄱ-ㅎ0-9., ]', '', cnt).strip() for cnt in content]).strip()
        if content != [] and re_content != '' and content != 'retry':
            if title:
                # re_title = re.sub('[^a-zA-Z가-힣ㄱ-ㅎ0-9., ]', '', title).strip()
                re_title = title.strip()
            else:
                re_title = ''
            item['title'] = re_title
            item['content'] = re_content
            item['photourl'] = photourl
            yield item
        elif content == 'retry':
            print('retry', response.meta["url"])
            with open('retry_kia_test.csv', 'a', encoding='utf-8') as f:
                f.write(','.join([response.url]) + ',' + response.meta["date"])
                f.write('\n')
        else:
            print('retry', response.meta["url"])
            with open('retry_kia_test.csv', 'a', encoding='utf-8') as f:
                f.write(','.join([response.url]) + ',' + response.meta["date"])
                f.write('\n')
