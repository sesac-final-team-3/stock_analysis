# Generated by Django 4.1.5 on 2023-01-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0002_tbforeignerinvestment_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tbohlcv",
            name="trading_value",
            field=models.BigIntegerField(
                blank=True, db_column="trading_value", null=True
            ),
        ),
    ]