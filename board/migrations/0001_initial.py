# Generated by Django 4.2.1 on 2023-05-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/%Y%m%d')),
                ('group_type', models.CharField(max_length=10)),
                ('field', models.CharField(max_length=10)),
                ('short_introduce', models.TextField(max_length=50)),
                ('natures', models.CharField(max_length=10)),
                ('recruitment_count', models.PositiveIntegerField()),
                ('deadline', models.DateField()),
                ('recruiting_url', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Natures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('mainphoto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
