# Generated by Django 2.2.13 on 2020-08-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200824_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referral_code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
