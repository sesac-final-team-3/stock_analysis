from django.db import models
from summary.models import TbName


# Create your models here.
class TbOHLCV(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)
	code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
	date = models.DateTimeField(db_column='date', blank=True, null=True)
	compare_price = models.FloatField(db_column='compare_price', blank=True, null=True)
	open_price = models.IntegerField(db_column='open_price', blank=True, null=True)
	high_price = models.IntegerField(db_column='high_price', blank=True, null=True)	
	low_price = models.IntegerField(db_column='low_price', blank=True, null=True)	
	close_price = models.IntegerField(db_column='close_price', blank=True, null=True)	
	trading_volume = models.IntegerField(db_column='trading_volume', blank=True, null=True)
	trading_value = models.IntegerField(db_column='trading_value', blank=True, null=True)

	class Meta:
		db_table = 'tb_ohlcv'
	

class TbFundamental(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)
	code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
	date = models.DateTimeField(db_column='date', blank=True, null=True)
	BPS = models.FloatField(db_column='BPS', blank=True, null=True)
	PER = models.FloatField(db_column='PER', blank=True, null=True)
	PBR = models.FloatField(db_column='PBR', blank=True, null=True)
	EPS = models.FloatField(db_column='EPS', blank=True, null=True)
	DIV = models.FloatField(db_column='DIV', blank=True, null=True)
	DPS = models.FloatField(db_column='DPS', blank=True, null=True)

	class Meta:
		db_table = 'tb_fundmental'
	

class TbProfit(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)
	code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
	date = models.DateTimeField(db_column='date', blank=True, null=True)
	profit = models.IntegerField(db_column='profit', blank=True, null=True)
	
	class Meta:
		db_table = 'tb_profit'


class TbShort(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)
	code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
	date = models.DateTimeField(db_column='date', blank=True, null=True)
	balance = models.IntegerField(db_column='balance', blank=True, null=True)
	volume = models.IntegerField(db_column='volume', blank=True, null=True)
	value = models.IntegerField(db_column='value', blank=True, null=True)
	market_cap = models.IntegerField(db_column='market_cap', blank=True, null=True)
	weight = models.IntegerField(db_column='weight', blank=True, null=True)


	class Meta:
		db_table = 'tb_short'


class TbTradingValue(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)
	code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
	date = models.DateTimeField(db_column='date', blank=True, null=True)
	institution = models.IntegerField(db_column='institution', blank=True, null=True)
	retail_investor = models.IntegerField(db_column='retail_investor', blank=True, null=True)
	etc_corporation = models.IntegerField(db_column='etc_corporation', blank=True, null=True)
	foreigner = models.IntegerField(db_column='foreigner', blank=True, null=True)


	class Meta:
		db_table = 'tb_tdvalue'


class TbTradingVolume(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)
	code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
	date = models.DateTimeField(db_column='date', blank=True, null=True)
	institution = models.IntegerField(db_column='institution', blank=True, null=True)
	retail_investor = models.IntegerField(db_column='retail_investor', blank=True, null=True)
	etc_corporation = models.IntegerField(db_column='etc_corporation', blank=True, null=True)
	foreigner = models.IntegerField(db_column='foreigner', blank=True, null=True)


	class Meta:
		db_table = 'tb_tdvolume'


class TbForeignerInvestment(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)
	code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
	volume = models.IntegerField(db_column='volume', blank=True, null=True)
	holding_volume = models.IntegerField(db_column='holding_volume', blank=True, null=True)
	shareholding = models.IntegerField(db_column='shareholding', blank=True, null=True)
	limit_volume = models.IntegerField(db_column='limit_volume', blank=True, null=True)
	exhaustion_rate = models.IntegerField(db_column='exhaustion_rate', blank=True, null=True)

	class Meta:
		db_table = 'tb_forinv'
