# Generated by Django 5.0 on 2024-03-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productaccessoriestable',
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
    ]
