# Generated by Django 3.2.5 on 2021-07-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210706_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='student_id',
            field=models.IntegerField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
