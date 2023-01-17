from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
# import os
# os.environ.get("DJANGO_SETTINGS_MODULE")

# import django
# django.setup()
# Create your models here.

class TbName(models.Model):
    code = models.CharField(db_column='code', max_length=16, blank=False, null=False, primary_key=True)
    name = models.CharField(db_column='name', max_length=16, blank=False, null=False)
    market=models.IntegerField(db_column='market',blank=False,null=False)
    sector = models.CharField(db_column='sector', max_length=64,blank=True, null=True)
    listed_date = models.DateTimeField(db_column='listed_date', blank=True, null=True)
    CEO = models.CharField(db_column='CEO', max_length=64, blank=True, null=True)
    homepage = models.CharField(db_column='homepage', max_length=64,blank=True, null=True)
    market_cap = models.BigIntegerField(db_column='market_cap', blank=True, null=True)
    updated_date = models.DateTimeField(db_column='updated_date', blank=True, null=True)  

    class Meta:
        db_table = 'tb_name'


class TbReport(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    date = models.DateTimeField(db_column='date', blank=True, null=True)
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
    firm = models.CharField(db_column='firm', max_length=16, blank=True, null=True)
    comment = models.CharField(db_column='comment', max_length=16, blank=True, null=True)
    price = models.CharField(db_column='price', max_length=16, blank=True, null=True)
    updated_date = models.DateTimeField(db_column='updated_date', blank=True, null=True) 

    class Meta:
        db_table = 'tb_report'

class TbSentimental(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    date = models.DateTimeField(db_column='date', blank=True, null=True)
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
    comment = models.TextField(db_column='comment', blank=True, null=True)
    updated_date = models.DateTimeField(db_column='updated_date', blank=True, null=True)
    news_graph=models.TextField(db_column='news_graph',blank=True,null=True)

    class Meta:
        db_table = 'tb_senti'

class TbOHLCV(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)
	date = models.DateTimeField(db_column='date', blank=True, null=True)
	code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
	compare_price = models.FloatField(db_column='compare_price', blank=True, null=True)
	open_price = models.IntegerField(db_column='open_price', blank=True, null=True)
	high_price = models.IntegerField(db_column='high_price', blank=True, null=True)	
	low_price = models.IntegerField(db_column='low_price', blank=True, null=True)	
	close_price = models.IntegerField(db_column='close_price', blank=True, null=True)	
	trading_volume = models.IntegerField(db_column='trading_volume', blank=True, null=True)
	trading_value = models.BigIntegerField(db_column='trading_value', blank=True, null=True)
	news_keyword = models.TextField(db_column='news_keyword', null=True, default=dict)
	BPS = models.FloatField(db_column='BPS', blank=True, null=True)
	PER = models.FloatField(db_column='PER', blank=True, null=True)
	PBR = models.FloatField(db_column='PBR', blank=True, null=True)
	EPS = models.FloatField(db_column='EPS', blank=True, null=True)
	DIVy = models.FloatField(db_column='DIVy', blank=True, null=True)
	DPS = models.FloatField(db_column='DPS', blank=True, null=True)
	updated_date = models.DateTimeField(db_column='updated_date', blank=True, null=True) 

	class Meta:
		db_table = 'tb_ohlcv'