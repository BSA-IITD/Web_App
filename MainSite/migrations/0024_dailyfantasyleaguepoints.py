# Generated by Django 2.0.6 on 2020-10-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0023_fantasyleaguematch_image_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyFantasyLeaguePoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('entryno', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(help_text='Email ID', max_length=30)),
                ('points', models.IntegerField(default=0, help_text='User points')),
            ],
        ),
    ]
