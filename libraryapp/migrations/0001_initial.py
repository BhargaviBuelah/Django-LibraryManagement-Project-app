# Generated by Django 4.1.1 on 2022-10-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=50)),
                ('bdesc', models.CharField(max_length=100)),
                ('bauthor', models.CharField(max_length=50)),
                ('copies', models.FloatField()),
                ('price', models.FloatField()),
                ('cat', models.CharField(max_length=10)),
            ],
        ),
    ]
