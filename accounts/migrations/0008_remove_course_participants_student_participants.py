# Generated by Django 4.0.6 on 2022-07-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_course_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='participants',
        ),
        migrations.AddField(
            model_name='student',
            name='participants',
            field=models.ManyToManyField(to='accounts.course'),
        ),
    ]
