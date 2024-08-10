# Generated by Django 5.1 on 2024-08-09 05:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xodim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familiya', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('lavozim', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Davomat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelgan_vaqti', models.DateTimeField(default=django.utils.timezone.now)),
                ('xodim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='davomat', to='dashboard.xodim')),
            ],
        ),
    ]
