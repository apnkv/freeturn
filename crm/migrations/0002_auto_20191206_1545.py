# Generated by Django 2.2.8 on 2019-12-06 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        ('crm', '0001_initial'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.ProjectPage'),
        ),
        migrations.AddField(
            model_name='invoicegenerationsettings',
            name='default_logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='invoicegenerationsettings',
            name='site',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='logo',
            field=models.ForeignKey(blank=True, help_text='Picture to use', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='crm.Project'),
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Company'),
        ),
        migrations.AddField(
            model_name='employee',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='cvgenerationsettings',
            name='default_picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='cvgenerationsettings',
            name='site',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site'),
        ),
        migrations.AddField(
            model_name='cv',
            name='picture',
            field=models.ForeignKey(blank=True, help_text='Picture to use', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='cv',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cvs', to='crm.Project'),
        ),
        migrations.AddField(
            model_name='cv',
            name='relevant_project_pages',
            field=models.ManyToManyField(blank=True, help_text='Project pages to be placed on the first page, eye catcher for this project', related_name='applications_highlighted', to='home.ProjectPage'),
        ),
        migrations.AddField(
            model_name='cv',
            name='relevant_skills',
            field=models.ManyToManyField(blank=True, help_text='Technologies to be included, will be automatically formed to look relevant', to='home.Technology'),
        ),
        migrations.AddField(
            model_name='company',
            name='channel',
            field=models.ForeignKey(blank=True, help_text='Lead channel this company came from', null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Channel'),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.City'),
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
    ]