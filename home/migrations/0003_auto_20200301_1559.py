# Generated by Django 2.2.9 on 2020-03-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200301_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='github_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='linkedin_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='stackoverflow_profile',
            field=models.URLField(blank=True, null=True),
        ),
    ]