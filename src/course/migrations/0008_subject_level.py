# Generated by Django 3.2.5 on 2021-07-07 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='course.level'),
            preserve_default=False,
        ),
    ]