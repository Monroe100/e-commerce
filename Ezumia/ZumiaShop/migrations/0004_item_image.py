# Generated by Django 2.2.10 on 2020-03-09 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZumiaShop', '0003_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='image', upload_to='products'),
            preserve_default=False,
        ),
    ]
