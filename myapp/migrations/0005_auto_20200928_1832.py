# Generated by Django 2.2.16 on 2020-09-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200924_0634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]