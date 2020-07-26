# Generated by Django 3.0.3 on 2020-04-05 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cyber_cell', '0016_delete_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Did', models.IntegerField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
