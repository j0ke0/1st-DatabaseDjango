# Generated by Django 4.1.6 on 2023-02-15 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysites', '0002_rename_datails_plandetails_details_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plandetails',
            old_name='details',
            new_name='detail',
        ),
        migrations.AddField(
            model_name='subscription',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysites.profile'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan_end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterUniqueTogether(
            name='plandetails',
            unique_together={('plan', 'detail')},
        ),
    ]