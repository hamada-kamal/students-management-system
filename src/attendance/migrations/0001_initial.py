# Generated by Django 3.2.5 on 2021-07-17 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0020_alter_subject_code'),
        ('accounts', '0007_alter_profile_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.level')),
                ('students', models.ManyToManyField(blank=True, null=True, to='accounts.Profile')),
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.subject')),
            ],
        ),
    ]
