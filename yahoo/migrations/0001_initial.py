# Generated by Django 2.1.4 on 2019-01-05 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='YahooExcludeSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_id', models.CharField(db_index=True, max_length=128, verbose_name='セラーID')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='メモ')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザ名')),
            ],
            options={
                'db_table': 'yahoo_exclude_seller',
            },
        ),
        migrations.CreateModel(
            name='YahooExcludeSellerMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_id', models.CharField(db_index=True, max_length=128, verbose_name='セラーID')),
            ],
            options={
                'verbose_name': '禁止セラー',
                'verbose_name_plural': '禁止セラー',
                'db_table': 'yahoo_exclude_seller_master',
            },
        ),
        migrations.CreateModel(
            name='YahooImportCSVResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.IntegerField(blank=True, null=True, verbose_name='正常処理件数')),
                ('error_record_numbers', models.IntegerField(blank=True, null=True, verbose_name='フォーマットエラー件数')),
                ('error_record_numbers_txt', models.TextField(blank=True, null=True, verbose_name='フォーマットエラー一覧')),
                ('duplicate_skus', models.IntegerField(blank=True, null=True, verbose_name='重複件数')),
                ('duplicate_skus_txt', models.TextField(blank=True, null=True, verbose_name='重複一覧')),
                ('over_skus', models.IntegerField(blank=True, null=True, verbose_name='登録オーバ件数')),
                ('over_skus_text', models.TextField(blank=True, null=True, verbose_name='登録オーバ一覧')),
                ('error_yahoo_items', models.IntegerField(blank=True, null=True, verbose_name='オークション該当商品無し')),
                ('error_yahoo_items_txt', models.TextField(blank=True, null=True, verbose_name='オークション該当商品無し')),
                ('error_asins', models.IntegerField(blank=True, null=True, verbose_name='ASINエラー')),
                ('error_asins_text', models.TextField(blank=True, null=True, verbose_name='ASINエラー一覧')),
                ('error_skus', models.IntegerField(blank=True, null=True, verbose_name='SKUエラー')),
                ('error_skus_text', models.TextField(blank=True, null=True, verbose_name='SKUエラー一覧')),
                ('status', models.IntegerField(blank=True, null=True, verbose_name='ステータス')),
                ('user_check', models.BooleanField(blank=True, null=True, verbose_name='ユーザ確認')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='完了日')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('result_message', models.TextField(blank=True, null=True, verbose_name='処理結果')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザ名')),
            ],
            options={
                'verbose_name': '商品取り込み履歴',
                'verbose_name_plural': '商品取り込み履歴',
                'db_table': 'yahoo_import_csv_result',
            },
        ),
        migrations.CreateModel(
            name='YahooToAmazonCSV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_type', models.IntegerField(verbose_name='出品種別')),
                ('file_name', models.CharField(max_length=64, verbose_name='ファイル名')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザ名')),
            ],
            options={
                'db_table': 'yahoo_to_amazon_csv',
            },
        ),
        migrations.CreateModel(
            name='YahooToAmazonItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_type', models.IntegerField(null=True, verbose_name='出品種別')),
                ('item_sku', models.CharField(db_index=True, max_length=64, null=True, verbose_name='出品者SKU')),
                ('item_name', models.CharField(db_index=True, max_length=256, null=True, verbose_name='商品名')),
                ('external_product_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='商品コード(JANコード等)')),
                ('external_product_id_type', models.CharField(blank=True, choices=[('EAN', 'EAN'), ('ISBN', 'ISBN'), ('UPC', 'UPC'), ('ASIN', 'ASIN'), ('GTIN', 'GTIN')], max_length=16, null=True, verbose_name='商品コードのタイプ')),
                ('brand_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='ブランド名')),
                ('manufacturer', models.CharField(blank=True, max_length=256, null=True, verbose_name='メーカー名')),
                ('feed_product_type', models.CharField(blank=True, max_length=64, null=True, verbose_name='商品タイプ')),
                ('part_number', models.CharField(blank=True, max_length=256, null=True, verbose_name='メーカー型番')),
                ('product_description', models.TextField(blank=True, null=True, verbose_name='商品説明文')),
                ('bullet_point', models.TextField(blank=True, null=True, verbose_name='商品の仕様')),
                ('model', models.CharField(blank=True, max_length=256, null=True, verbose_name='型番')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='在庫数(登録時)')),
                ('fulfillment_latency', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='リードタイム(登録時)')),
                ('condition_type', models.CharField(blank=True, choices=[('New', '新品'), ('Refurbished', '再生品'), ('UsedLikeNew', '中古-ほぼ新品'), ('UsedVeryGood', '中古-非常に良い'), ('UsedGood', '中古-良い'), ('UsedAcceptable', '中古-可'), ('CollectibleLikeNew', 'コレクター商品-ほぼ新品'), ('CollectibleVeryGood', 'コレクター商品-非常に良い'), ('CollectibleGood', 'コレクター商品-良い'), ('CollectibleAcceptable', 'コレクター商品-可')], max_length=32, null=True, verbose_name='商品のコンディション')),
                ('standard_price', models.IntegerField(null=True, verbose_name='商品の販売価格')),
                ('standard_price_points', models.IntegerField(blank=True, null=True, verbose_name='ポイント')),
                ('condition_note', models.TextField(null=True, verbose_name='商品のコンディション説明')),
                ('item_weight', models.IntegerField(blank=True, null=True, verbose_name='商品の重量')),
                ('item_weight_unit_of_measure', models.CharField(blank=True, max_length=16, null=True, verbose_name='商品の重量の単位')),
                ('item_height', models.IntegerField(blank=True, null=True, verbose_name='商品の高さ')),
                ('item_length', models.IntegerField(blank=True, null=True, verbose_name='商品の長さ')),
                ('item_width', models.IntegerField(blank=True, null=True, verbose_name='商品の幅')),
                ('item_length_unit_of_measure', models.CharField(blank=True, max_length=16, null=True, verbose_name='商品寸法の単位')),
                ('recommended_browse_nodes', models.CharField(blank=True, max_length=64, null=True, verbose_name='推奨ブラウズノード')),
                ('generic_keywords', models.CharField(blank=True, max_length=256, null=True, verbose_name='検索キーワード')),
                ('main_image_url', models.CharField(max_length=256, null=True, verbose_name='商品メイン画像URL')),
                ('other_image_url1', models.CharField(blank=True, max_length=256, null=True, verbose_name='商品サブ画像URL1')),
                ('other_image_url2', models.CharField(blank=True, max_length=256, null=True, verbose_name='商品サブ画像URL2')),
                ('other_image_url3', models.CharField(blank=True, max_length=256, null=True, verbose_name='商品サブ画像URL3')),
                ('csv_flag', models.IntegerField(db_index=True, null=True, verbose_name='CSV出力状態')),
                ('format', models.CharField(blank=True, db_index=True, max_length=32, null=True, verbose_name='フォーマット')),
                ('category', models.CharField(blank=True, max_length=32, null=True, verbose_name='カテゴリー')),
                ('purchaseo_seller_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='セーラーID(初回仕入れ時)')),
                ('purchase_item_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='商品ID(登録時)')),
                ('purchase_quantity', models.IntegerField(blank=True, null=True, verbose_name='仕入数(初回仕入れ時)')),
                ('purchase_fulfillment_latency', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='リードタイム(初回仕入れ時)')),
                ('purchase_price', models.IntegerField(blank=True, null=True, verbose_name='仕入れ価格(初回仕入れ時)')),
                ('purchase_similarity', models.FloatField(blank=True, null=True, verbose_name='類似度(初回仕入れ時)')),
                ('current_purchase_seller_id', models.CharField(blank=True, db_index=True, max_length=32, null=True, verbose_name='セーラーID(現在)')),
                ('current_purchase_item_id', models.CharField(blank=True, db_index=True, max_length=32, null=True, verbose_name='商品ID(現在)')),
                ('current_purchase_quantity', models.IntegerField(blank=True, null=True, verbose_name='仕入数(現在)')),
                ('current_purchase_fulfillment_latency', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='リードタイム(現在)')),
                ('current_purchase_price', models.IntegerField(blank=True, null=True, verbose_name='仕入れ価格(現在)')),
                ('current_similarity', models.FloatField(blank=True, null=True, verbose_name='類似度(現在)')),
                ('amazon_price', models.IntegerField(blank=True, null=True, verbose_name='アマゾン最安値')),
                ('update_fulfillment_latency_request', models.BooleanField(blank=True, db_index=True, null=True, verbose_name='リードタイム更新要求')),
                ('research_request', models.BooleanField(blank=True, db_index=True, null=True, verbose_name='在庫検索要求')),
                ('update_quantity_request', models.BooleanField(blank=True, db_index=True, null=True, verbose_name='在庫更新要求')),
                ('record_type', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='レコードタイプ')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザ名')),
            ],
            options={
                'db_table': 'yahoo_to_amazon_item',
            },
        ),
    ]
