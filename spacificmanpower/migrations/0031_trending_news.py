# Generated by Django 4.0.6 on 2023-04-06 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spacificmanpower', '0030_alter_seeker_profile_is_annually_monthly'),
    ]

    operations = [
        migrations.CreateModel(
            name='trending_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=100)),
                ('news_description', models.CharField(max_length=50)),
                ('news_image', models.ImageField(max_length=50, upload_to='')),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('modifiedDate', models.DateTimeField(auto_now=True)),
                ('user_account_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_account_id_trending_news', to='spacificmanpower.user_account')),
            ],
        ),
    ]
