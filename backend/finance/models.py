from django.db import models
from summary.models import TbName


# Create your models here.
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
	count = models.CharField(db_column='count', max_length=64, blank=True, null=True)
	predict = models.CharField(db_column='predict', max_length=16, blank=True, null=True)
	BPS = models.FloatField(db_column='BPS', blank=True, null=True)
	PER = models.FloatField(db_column='PER', blank=True, null=True)
	PBR = models.FloatField(db_column='PBR', blank=True, null=True)
	EPS = models.FloatField(db_column='EPS', blank=True, null=True)
	DIVy = models.FloatField(db_column='DIVy', blank=True, null=True)
	DPS = models.FloatField(db_column='DPS', blank=True, null=True)
	updated_date = models.DateTimeField(db_column='updated_date', blank=True, null=True)

	class Meta:
		db_table = 'tb_ohlcv'
	

class TbTradingInfo(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)
	date = models.DateTimeField(db_column='date', blank=True, null=True)
	code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
	val_institution = models.BigIntegerField(db_column='val_institution', blank=True, null=True)
	val_retail_investor = models.BigIntegerField(db_column='val_retail_investor', blank=True, null=True)
	val_etc_corporation = models.BigIntegerField(db_column='val_etc_corporation', blank=True, null=True)
	val_foreigner = models.BigIntegerField(db_column='val_foreigner', blank=True, null=True)
	vol_institution = models.BigIntegerField(db_column='vol_institution', blank=True, null=True)
	vol_retail_investor = models.BigIntegerField(db_column='vol_retail_investor', blank=True, null=True)
	vol_etc_corporation = models.BigIntegerField(db_column='vol_etc_corporation', blank=True, null=True)
	vol_foreigner = models.BigIntegerField(db_column='vol_foreigner', blank=True, null=True)
	holding_volume = models.BigIntegerField(db_column='holding_volume', blank=True, null=True)
	shareholding = models.BigIntegerField(db_column='shareholding', blank=True, null=True)
	limit_volume = models.BigIntegerField(db_column='limit_volume', blank=True, null=True)
	exhaustion_rate = models.BigIntegerField(db_column='exhaustion_rate', blank=True, null=True)
	short_balance = models.BigIntegerField(db_column='short_balance', blank=True, null=True)
	short_value = models.BigIntegerField(db_column='short_value', blank=True, null=True)
	short_weight = models.BigIntegerField(db_column='short_weight', blank=True, null=True)
	updated_date = models.DateTimeField(db_column='updated_date', blank=True, null=True)

	class Meta:
		db_table = 'tb_tradinfo'
	

class TbProfit(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)
	date = models.IntegerField(db_column='date', blank=True, null=True)
	code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
	profit = models.IntegerField(db_column='profit', blank=True, null=True)
	updated_date = models.DateTimeField(db_column='updated_date', blank=True, null=True) 

	class Meta:
		db_table = 'tb_profit'