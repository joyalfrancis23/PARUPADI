# Generated by Django 3.2.3 on 2021-05-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpage', '0004_auto_20210524_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='Time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
