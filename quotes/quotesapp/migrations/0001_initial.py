# Generated by Django 4.1.6 on 2023-02-06 11:47

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('born_date', models.DateField()),
                ('born_location', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5900)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('quote', models.CharField(max_length=999)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotesapp.author')),
            ],
        ),
    ]