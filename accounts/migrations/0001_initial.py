# Generated by Django 5.0 on 2025-01-15 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('purchase_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('available_slots', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('spotify_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.spotifyaccount')),
            ],
        ),
    ]