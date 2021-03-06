# Generated by Django 2.2.10 on 2020-03-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZumiaShop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sports wear'), ('OW', 'Outwear')], default='P', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary'), ('D', 'Danger')], default='p', max_length=1),
            preserve_default=False,
        ),
    ]
