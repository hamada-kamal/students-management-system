# Generated by Django 3.2.5 on 2021-07-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_delete_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='level',
            field=models.CharField(choices=[('Primary', 'Primary'), ('level1', 'level1'), ('level2', 'level2'), ('level3', 'level3'), ('level4', 'level4')], default='', max_length=50),
            preserve_default=False,
        ),
    ]
