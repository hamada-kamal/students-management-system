# Generated by Django 3.2.5 on 2021-07-07 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_remove_subject_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
