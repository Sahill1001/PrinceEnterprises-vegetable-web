# Generated by Django 4.1.1 on 2022-11-18 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_contact_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='state',
            new_name='last_name',
        ),
    ]
