# Generated by Django 2.0.7 on 2018-07-24 15:00

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180724_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='responsibility',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
