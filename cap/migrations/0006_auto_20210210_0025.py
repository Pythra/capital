# Generated by Django 3.1.6 on 2021-02-09 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap', '0005_auto_20210207_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='total',
            field=models.DecimalField(decimal_places=0, max_digits=9),
        ),
    ]
