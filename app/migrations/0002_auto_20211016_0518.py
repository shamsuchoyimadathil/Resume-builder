# Generated by Django 3.2.8 on 2021-10-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume_model',
            old_name='degree',
            new_name='qualification',
        ),
        migrations.AlterField(
            model_name='resume_model',
            name='awards',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
