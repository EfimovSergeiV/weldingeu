# Generated by Django 4.1.3 on 2022-11-18 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_name_productmodeltranslation_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodeltranslation',
            old_name='title',
            new_name='name',
        ),
    ]
