# Generated by Django 4.1.1 on 2022-11-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_product_description_product_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]