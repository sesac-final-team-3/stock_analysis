from django.db import models
from summary.models import TbName


class TbNews(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
    press = models.CharField(db_column='press', max_length=16, blank=True, null=True)
    date = models.DateTimeField(db_column='date', blank=True, null=True)
    date_cate = models.DateTimeField(db_column='date_cate', blank=True, null=True)
    url = models.TextField(db_column='url', blank=True, null=True)
    content = models.TextField(db_column='content', blank=True, null=True)
    target = models.IntegerField(db_column='target', blank=True, null=True)
    photourl = models.CharField(db_column='photourl', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tb_news'