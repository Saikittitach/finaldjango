# Generated by Django 2.2.16 on 2020-10-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200928_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatabase',
            name='phone',
            field=models.TextField(max_length=20),
        ),
    ]
