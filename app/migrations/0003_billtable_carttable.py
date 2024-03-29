# Generated by Django 5.0 on 2024-03-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_productaccessoriestable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productid', models.IntegerField()),
                ('Productname', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('Userid', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Firstname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Carttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productid', models.IntegerField()),
                ('Productname', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('Userid', models.CharField(max_length=100)),
            ],
        ),
    ]
