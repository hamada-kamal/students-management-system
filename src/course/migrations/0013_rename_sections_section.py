# Generated by Django 3.2.5 on 2021-07-08 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_lab_sections'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sections',
            new_name='Section',
        ),
    ]
