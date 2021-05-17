# Generated by Django 2.2.13 on 2020-12-22 09:49

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFileSync',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('input_filename', models.CharField(db_index=True, max_length=255)),
                ('dry_run', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('started', 'STARTED'), ('finished', 'FINISHED'), ('failed', 'FAILED')], default='started', max_length=10)),
                ('output_log', models.TextField(blank=True)),
                ('processed_count', models.IntegerField(default=0)),
            ],
            options={
                'base_manager_name': 'executions',
                'default_manager_name': 'executions',
            },
            managers=[
                ('executions', django.db.models.manager.Manager()),
            ],
        ),
    ]
