# Generated by Django 3.2.16 on 2022-12-22 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_alter_project_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['pk']},
        ),
    ]
