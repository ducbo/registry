# Generated by Django 2.2.10 on 2020-05-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0025_auto_20200314_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='auto_renew_enabled',
            field=models.BooleanField(default=False, help_text='Domain will be automatically renewed 3 months before the expiration date, if you have enough funds. Account balance will be automatically deducted.', verbose_name='Automatically renew'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='automatic_renewal_enabled',
            field=models.BooleanField(default=False, help_text='Your domains will be automatically renewed 3 months before the expiration date, if you have enough funds. Account balance will be automatically deducted.', verbose_name='Automatically renew expiring domains'),
        ),
    ]
