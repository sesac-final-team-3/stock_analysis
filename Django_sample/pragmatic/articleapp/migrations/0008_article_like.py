# Generated by Django 3.2.16 on 2022-12-31 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0007_remove_article_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]