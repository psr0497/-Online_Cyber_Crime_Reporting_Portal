# Generated by Django 3.0.3 on 2020-04-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber_cell', '0013_auto_20200404_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='image',
            field=models.ImageField(max_length=255, upload_to=' '),
        ),
    ]
