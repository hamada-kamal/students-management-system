# Generated by Django 3.2.5 on 2021-07-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210706_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AlterField(
            model_name='profile',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]
