# Generated by Django 4.0.6 on 2023-04-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacificmanpower', '0014_alter_user_log_last_login_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_log',
            name='last_job_apply_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]