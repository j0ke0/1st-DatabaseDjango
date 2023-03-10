# Generated by Django 4.1.6 on 2023-02-18 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysites', '0005_remove_subscription_profile_access'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='plan_end_date',
        ),
        migrations.AddField(
            model_name='subscription',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='expire_hour',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
