# Generated by Django 3.2.5 on 2021-07-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_subject_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
