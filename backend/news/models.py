from django.db import models
from summary.models import TbName


class TbNews(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    date = models.DateTimeField(db_column='date', blank=True, null=True)
    code = models.ForeignKey(TbName, models.DO_NOTHING, db_column='code')
    press = models.CharField(db_column='press', max_length=16, blank=True, null=True)
    url = models.TextField(db_column='url', blank=True, null=True)
    title = models.CharField(db_column='title', max_length=64, blank=True, null=True)
    content = models.TextField(db_column='content', blank=True, null=True)
    photourl = models.TextField(db_column='photourl', blank=True, null=True)
    graph = models.TextField(db_column='graph', blank=True, null=True)
    updated_date = models.DateTimeField(db_column='updated_date', blank=True, null=True)

    class Meta:
        db_table = 'tb_news'
