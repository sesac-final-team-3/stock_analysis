# Generated by Django 3.2.16 on 2022-12-22 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['pk']},
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set(),
        ),
    ]
