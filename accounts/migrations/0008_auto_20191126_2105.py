# Generated by Django 2.1.4 on 2019-11-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_overrideconstantvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcandidatetocsv',
            name='max_output',
            field=models.IntegerField(default=0, verbose_name='1日に出力可能な最大アイテム数'),
        ),
        migrations.AddField(
            model_name='itemcandidatetocsv',
            name='today_output',
            field=models.IntegerField(default=0, verbose_name='今日出力したアイテム数'),
        ),
        migrations.AlterField(
            model_name='itemcandidatetocsv',
            name='max_output_mercari',
            field=models.IntegerField(default=0, verbose_name='1日に出力可能な最大Mercariアイテム数(未使用)'),
        ),
        migrations.AlterField(
            model_name='itemcandidatetocsv',
            name='max_output_yahoo',
            field=models.IntegerField(default=0, verbose_name='1日に出力可能な最大Yahooアイテム数(未使用)'),
        ),
        migrations.AlterField(
            model_name='itemcandidatetocsv',
            name='today_output_mercari',
            field=models.IntegerField(default=0, verbose_name='今日出力したMercariアイテム数(未使用)'),
        ),
        migrations.AlterField(
            model_name='itemcandidatetocsv',
            name='today_output_yahoo',
            field=models.IntegerField(default=0, verbose_name='今日出力したYahooアイテム数(未使用)'),
        ),
    ]
