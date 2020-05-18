# Generated by Django 2.2.12 on 2020-05-06 14:27

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20200506_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='notes',
            field=wagtail.core.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='payment_address',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='contact_details',
            field=wagtail.core.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='cv',
            name='education_overview',
            field=wagtail.core.fields.RichTextField(help_text='Notice on your education'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='experience_overview',
            field=wagtail.core.fields.RichTextField(help_text='Notice on your experience'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='languages_overview',
            field=wagtail.core.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='cv',
            name='rate_overview',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='working_permit',
            field=wagtail.core.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='cvgenerationsettings',
            name='default_contact_details',
            field=wagtail.core.fields.RichTextField(default='sergey@cheparev.com'),
        ),
        migrations.AlterField(
            model_name='cvgenerationsettings',
            name='default_education_overview',
            field=wagtail.core.fields.RichTextField(default='Novosibirsk State Technical University', help_text='Notice on your education'),
        ),
        migrations.AlterField(
            model_name='cvgenerationsettings',
            name='default_experience_overview',
            field=wagtail.core.fields.RichTextField(default='Python developer experience: 7 years', help_text='Notice on your experience'),
        ),
        migrations.AlterField(
            model_name='cvgenerationsettings',
            name='default_languages_overview',
            field=wagtail.core.fields.RichTextField(default='English: fluent'),
        ),
        migrations.AlterField(
            model_name='cvgenerationsettings',
            name='default_rate_overview',
            field=wagtail.core.fields.RichTextField(default='<<change default in settings>>'),
        ),
        migrations.AlterField(
            model_name='cvgenerationsettings',
            name='default_working_permit',
            field=wagtail.core.fields.RichTextField(default='PERMANENT RESIDENCE'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_account',
            field=wagtail.core.fields.RichTextField(help_text='Payment bank account details'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='contact_data',
            field=wagtail.core.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_address',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Copied from the company, if empty'),
        ),
        migrations.AlterField(
            model_name='invoicegenerationsettings',
            name='default_bank_account',
            field=wagtail.core.fields.RichTextField(help_text='Payment bank account details'),
        ),
        migrations.AlterField(
            model_name='invoicegenerationsettings',
            name='default_contact_data',
            field=wagtail.core.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='notes',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]