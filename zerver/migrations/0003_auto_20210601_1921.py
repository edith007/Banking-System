# Generated by Django 3.2.3 on 2021-06-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0002_bankdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='city',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='district',
            field=models.CharField(max_length=55),
        ),
    ]