# Generated by Django 5.1.4 on 2025-01-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='otp_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
