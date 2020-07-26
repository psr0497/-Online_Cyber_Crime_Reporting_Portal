# Generated by Django 3.0.3 on 2020-04-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber_cell', '0006_delete_case'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rname', models.CharField(max_length=30)),
                ('remail', models.CharField(max_length=30)),
                ('rphone', models.IntegerField(max_length=15)),
                ('vname', models.CharField(max_length=30)),
                ('vemail', models.CharField(max_length=30)),
                ('vphone', models.IntegerField(max_length=15)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='static/victim/')),
                ('address', models.CharField(max_length=30)),
                ('other', models.CharField(max_length=30)),
                ('status', models.CharField(default='In_Progress', max_length=30)),
            ],
        ),
    ]
