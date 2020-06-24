# Generated by Django 3.0.6 on 2020-06-24 06:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studious', '0007_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleupdate',
            name='edit_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articleupdate',
            name='is_merged',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
