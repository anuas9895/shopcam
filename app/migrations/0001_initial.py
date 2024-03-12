# Generated by Django 5.0 on 2024-02-29 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productid', models.IntegerField()),
                ('Productname', models.CharField(max_length=100)),
                ('Image', models.FileField(upload_to='')),
                ('Quantity', models.IntegerField()),
                ('Unitprice', models.IntegerField()),
                ('Brand', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Signintable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Type', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Signuptable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Mobile', models.IntegerField()),
                ('Email', models.EmailField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Pincode', models.IntegerField()),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Type', models.CharField(blank=True, max_length=100)),
                ('Loginid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.signintable')),
            ],
        ),
    ]
