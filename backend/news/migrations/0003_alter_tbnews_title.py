# Generated by Django 3.2.16 on 2023-01-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_tbnews_photourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbnews',
            name='title',
            field=models.TextField(blank=True, db_column='title', null=True),
        ),
    ]