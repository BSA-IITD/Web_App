# Generated by Django 2.0.6 on 2020-06-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0015_auto_20200609_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='swimmingUserConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(help_text='Email', max_length=30)),
                ('code', models.CharField(help_text='Email', max_length=15)),
            ],
        ),
    ]
