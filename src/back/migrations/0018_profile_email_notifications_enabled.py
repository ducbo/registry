# Generated by Django 2.2.4 on 2019-10-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0017_auto_20190901_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_notifications_enabled',
            field=models.BooleanField(default=True, verbose_name='Email notifications'),
        ),
    ]