# Generated by Django 5.1.4 on 2024-12-11 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ifsc', models.CharField(max_length=11, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='api.bank')),
            ],
        ),
    ]
