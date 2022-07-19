# Generated by Django 2.0.6 on 2018-07-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0004_event_long_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='type',
            field=models.CharField(choices=[('Secretary', 'Secretary'), ('Executive', 'Executive'), ('Faculty', 'Faculty'), ('Captain', 'Captain'), ('Vice-Captain', 'Vice-Captain')], default='Secretary', max_length=15),
        ),
    ]
