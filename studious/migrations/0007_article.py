# Generated by Django 3.0.6 on 2020-06-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studious', '0006_org_index_by_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmcid', models.IntegerField()),
                ('doi', models.CharField(max_length=48)),
                ('journal_title', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=250)),
                ('journal_year', models.SmallIntegerField()),
                ('int_open_data', models.IntegerField()),
                ('int_data_share', models.IntegerField()),
            ],
        ),
    ]