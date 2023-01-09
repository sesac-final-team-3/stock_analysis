# Generated by Django 4.1.4 on 2023-01-09 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TbName",
            fields=[
                (
                    "code",
                    models.CharField(
                        db_column="code",
                        max_length=16,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(db_column="name", max_length=16)),
                ("market", models.IntegerField(db_column="market")),
                (
                    "sector",
                    models.CharField(
                        blank=True, db_column="sector", max_length=32, null=True
                    ),
                ),
                (
                    "listed_date",
                    models.DateTimeField(
                        blank=True, db_column="listed_date", null=True
                    ),
                ),
                (
                    "CEO",
                    models.CharField(
                        blank=True, db_column="CEO", max_length=64, null=True
                    ),
                ),
                (
                    "homepage",
                    models.CharField(
                        blank=True, db_column="homepage", max_length=64, null=True
                    ),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="volume", null=True),
                ),
                (
                    "updated_date",
                    models.DateTimeField(
                        blank=True, db_column="updated_date", null=True
                    ),
                ),
            ],
            options={"db_table": "tb_name",},
        ),
        migrations.CreateModel(
            name="TbSentimental",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="ID", primary_key=True, serialize=False),
                ),
                ("news", models.TextField(blank=True, db_column="news", null=True)),
                (
                    "comment",
                    models.JSONField(blank=True, db_column="comment", null=True),
                ),
                (
                    "updated_date",
                    models.DateTimeField(
                        blank=True, db_column="updated_date", null=True
                    ),
                ),
                (
                    "code",
                    models.ForeignKey(
                        db_column="code",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="summary.tbname",
                    ),
                ),
            ],
            options={"db_table": "tb_senti",},
        ),
        migrations.CreateModel(
            name="TbReport",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="ID", primary_key=True, serialize=False),
                ),
                ("date", models.DateTimeField(blank=True, db_column="date", null=True)),
                (
                    "firm",
                    models.CharField(
                        blank=True, db_column="firm", max_length=16, null=True
                    ),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True, db_column="comment", max_length=8, null=True
                    ),
                ),
                (
                    "price",
                    models.IntegerField(blank=True, db_column="price", null=True),
                ),
                (
                    "updated_date",
                    models.DateTimeField(
                        blank=True, db_column="updated_date", null=True
                    ),
                ),
                (
                    "code",
                    models.ForeignKey(
                        db_column="code",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="summary.tbname",
                    ),
                ),
            ],
            options={"db_table": "tb_report",},
        ),
    ]
