# Generated by Django 3.1.4 on 2020-12-16 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('website', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=5000)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('resort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='resorts.resort')),
            ],
        ),
    ]
