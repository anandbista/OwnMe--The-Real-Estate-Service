# Generated by Django 3.1.14 on 2022-07-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_auto_20220724_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_for',
            field=models.CharField(choices=[('S', 'Sell'), ('R', 'Rent')], default='S', max_length=5, verbose_name='Listing for'),
        ),
    ]