from django.db import models

# Create your models here.

class TbName(models.Model):
    code = models.CharField(db_column='code', max_length=16, blank=False, null=False, primary_key=True)
    name = models.CharField(db_column='name', max_length=16, blank=False, null=False)

    class Meta:
        db_table = 'tb_name'

class TbInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
    established_date = models.DateTimeField(db_column='established_date', blank=True, null=True)
    listed_date = models.DateTimeField(db_column='listed_date', blank=True, null=True)
    CEO = models.CharField(db_column='CEO',max_length=8, blank=True, null=True)
    settlement_date = models.DateTimeField(db_column='settlement_date', blank=True, null=True)
    tel = models.CharField(db_column='tel', max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'tb_info'

class TbReport(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
    title = models.CharField(db_column='title', max_length=255, blank=True, null=True)
    content = models.TextField(db_column='content', blank=True, null=True)
    date = models.DateTimeField(db_column='date', blank=True, null=True)
    firm = models.CharField(db_column='firm', max_length=16, blank=True, null=True)
    comment = models.CharField(db_column='comment', max_length=8, blank=True, null=True)
    price = models.IntegerField(db_column='price', blank=True, null=True)

    class Meta:
        db_table = 'tb_report'

class TbKeyword(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
    date = models.DateTimeField(db_column='date', blank=True, null=True)
    keyword = models.JSONField(db_column='keyword', blank=True, null=True)

    class Meta:
        db_table = 'tb_keyword'

class TbSentimental(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
    news = models.JSONField(db_column='news', blank=True, null=True)
    report = models.JSONField(db_column='report', blank=True, null=True)
    comment = models.JSONField(db_column='comment', blank=True, null=True)

    class Meta:
        db_table = 'tb_senti'