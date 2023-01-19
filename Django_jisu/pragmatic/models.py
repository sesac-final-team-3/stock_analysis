# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class TbName(models.Model):
    code = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=16)
    market = models.IntegerField()
    sector = models.CharField(max_length=64, blank=True, null=True)
    listed_date = models.DateTimeField(blank=True, null=True)
    ceo = models.CharField(db_column='CEO', max_length=64, blank=True, null=True)  # Field name made lowercase.
    homepage = models.CharField(max_length=64, blank=True, null=True)
    market_cap = models.BigIntegerField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_name'


class TbNews(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    press = models.CharField(max_length=16, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    photourl = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_news'


class TbOhlcv(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    compare_price = models.FloatField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    trading_volume = models.IntegerField(blank=True, null=True)
    trading_value = models.BigIntegerField(blank=True, null=True)
    news_keyword = models.TextField(blank=True, null=True)
    bps = models.FloatField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    per = models.FloatField(db_column='PER', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    eps = models.FloatField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    dps = models.FloatField(db_column='DPS', blank=True, null=True)  # Field name made lowercase.
    divy = models.FloatField(db_column='DIVy', blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=64, blank=True, null=True)
    predict = models.CharField(max_length=16, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ohlcv'


class TbProfit(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code', blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    profit = models.IntegerField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_profit'


class TbReport(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    firm = models.CharField(max_length=16, blank=True, null=True)
    comment = models.CharField(max_length=16, blank=True, null=True)
    price = models.CharField(max_length=16, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_report'


class TbSenti(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_senti'


class TbTradinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    val_institution = models.BigIntegerField(blank=True, null=True)
    val_retail_investor = models.BigIntegerField(blank=True, null=True)
    val_etc_corporation = models.BigIntegerField(blank=True, null=True)
    val_foreigner = models.BigIntegerField(blank=True, null=True)
    vol_institution = models.BigIntegerField(blank=True, null=True)
    vol_retail_investor = models.BigIntegerField(blank=True, null=True)
    vol_etc_corporation = models.BigIntegerField(blank=True, null=True)
    vol_foreigner = models.BigIntegerField(blank=True, null=True)
    holding_volume = models.BigIntegerField(blank=True, null=True)
    shareholding = models.BigIntegerField(blank=True, null=True)
    limit_volume = models.BigIntegerField(blank=True, null=True)
    exhaustion_rate = models.BigIntegerField(blank=True, null=True)
    short_balance = models.BigIntegerField(blank=True, null=True)
    short_value = models.BigIntegerField(blank=True, null=True)
    short_weight = models.BigIntegerField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_tradinfo'
