# Generated by Django 3.2.5 on 2021-07-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_subject_code'),
        ('home', '0004_registraion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registraion',
            name='subjects',
            field=models.ManyToManyField(blank=True, null=True, to='course.Subject'),
        ),
    ]
