# Generated by Django 3.2.3 on 2021-06-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0003_auto_20210601_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='branch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='district',
            field=models.CharField(max_length=100),
        ),
    ]
