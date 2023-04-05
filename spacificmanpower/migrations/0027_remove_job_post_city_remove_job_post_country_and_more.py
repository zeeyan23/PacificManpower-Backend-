# Generated by Django 4.0.6 on 2023-04-05 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spacificmanpower', '0026_alter_job_post_activity_job_post_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_post',
            name='city',
        ),
        migrations.RemoveField(
            model_name='job_post',
            name='country',
        ),
        migrations.RemoveField(
            model_name='job_post',
            name='state',
        ),
        migrations.RemoveField(
            model_name='job_post',
            name='street_address',
        ),
        migrations.RemoveField(
            model_name='job_post',
            name='zip',
        ),
        migrations.AlterField(
            model_name='job_post_activity',
            name='job_post_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='job_post_id', to='spacificmanpower.job_post'),
        ),
        migrations.AlterField(
            model_name='job_post_activity',
            name='user_account_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_account_idssss', to='spacificmanpower.user_account'),
        ),
        migrations.AlterField(
            model_name='job_post_skill_set',
            name='job_post_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_post_id_job_post_skill_set', to='spacificmanpower.job_post'),
        ),
        migrations.AlterField(
            model_name='job_post_skill_set',
            name='skill_set_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skill_set_id', to='spacificmanpower.skill_set'),
        ),
    ]
