# Generated by Django 4.1.4 on 2023-01-19 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0009_tbohlcv_updated_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="exhaustion_rate",
            field=models.BigIntegerField(
                blank=True, db_column="exhaustion_rate", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="holding_volume",
            field=models.BigIntegerField(
                blank=True, db_column="holding_volume", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="limit_volume",
            field=models.BigIntegerField(
                blank=True, db_column="limit_volume", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="shareholding",
            field=models.BigIntegerField(
                blank=True, db_column="shareholding", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="short_balance",
            field=models.BigIntegerField(
                blank=True, db_column="short_balance", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="short_value",
            field=models.BigIntegerField(
                blank=True, db_column="short_value", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="short_weight",
            field=models.BigIntegerField(
                blank=True, db_column="short_weight", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="val_etc_corporation",
            field=models.BigIntegerField(
                blank=True, db_column="val_etc_corporation", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="val_foreigner",
            field=models.BigIntegerField(
                blank=True, db_column="val_foreigner", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="val_institution",
            field=models.BigIntegerField(
                blank=True, db_column="val_institution", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="val_retail_investor",
            field=models.BigIntegerField(
                blank=True, db_column="val_retail_investor", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="vol_etc_corporation",
            field=models.BigIntegerField(
                blank=True, db_column="vol_etc_corporation", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="vol_foreigner",
            field=models.BigIntegerField(
                blank=True, db_column="vol_foreigner", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="vol_institution",
            field=models.BigIntegerField(
                blank=True, db_column="vol_institution", null=True
            ),
        ),
        migrations.AlterField(
            model_name="tbtradinginfo",
            name="vol_retail_investor",
            field=models.BigIntegerField(
                blank=True, db_column="vol_retail_investor", null=True
            ),
        ),
    ]
