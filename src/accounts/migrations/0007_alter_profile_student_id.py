# Generated by Django 3.2.5 on 2021-07-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210707_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='student_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
