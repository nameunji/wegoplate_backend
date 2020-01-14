# Generated by Django 3.0.1 on 2020-01-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20200108_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant_info',
            name='breaktime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurant_info',
            name='info',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant_info',
            name='last_order',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant_info',
            name='number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant_info',
            name='opening_horus',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurant_info',
            name='parking',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant_info',
            name='site',
            field=models.URLField(max_length=2500, null=True),
        ),
    ]