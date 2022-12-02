# Generated by Django 4.1.1 on 2022-10-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_description',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_date',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='subCategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
