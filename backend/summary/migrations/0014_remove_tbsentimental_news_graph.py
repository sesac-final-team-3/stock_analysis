# Generated by Django 4.1.4 on 2023-01-18 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("summary", "0013_remove_tbsentimental_news_keyword"),
    ]

    operations = [
        migrations.RemoveField(model_name="tbsentimental", name="news_graph",),
    ]
