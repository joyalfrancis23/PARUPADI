# Generated by Django 3.2.3 on 2021-05-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpage', '0002_alter_eventpage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='Date_Time',
            field=models.DateTimeField(blank=True),
        ),
    ]
