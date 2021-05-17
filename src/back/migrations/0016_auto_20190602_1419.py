# Generated by Django 2.2 on 2019-06-02 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0015_auto_20190523_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='contact_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='admin_domains', to='back.Contact', verbose_name='Administrative contact'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='contact_billing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='billing_domains', to='back.Contact', verbose_name='Billing contact'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='contact_tech',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tech_domains', to='back.Contact', verbose_name='Technical contact'),
        ),
    ]
