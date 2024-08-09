# Generated by Django 4.2.3 on 2024-08-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('account_no', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('customer_id', models.ImageField(upload_to='')),
                ('branch', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('adhar_sub', models.IntegerField()),
                ('adhar_nom', models.IntegerField()),
                ('insured_name', models.CharField(max_length=255)),
                ('nom_account', models.IntegerField()),
                ('nom_name', models.CharField(max_length=255)),
                ('bank', models.IntegerField()),
                ('status', models.CharField(choices=[], max_length=50)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
    ]
