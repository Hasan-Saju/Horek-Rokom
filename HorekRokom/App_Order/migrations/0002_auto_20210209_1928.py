# Generated by Django 3.1.4 on 2021-02-09 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='oredered',
            new_name='ordered',
        ),
    ]